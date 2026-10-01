"""Legacy Re=1000 entry point; delegates to the reusable cavity analyzer."""

from __future__ import annotations

import argparse
import csv
import math
import re
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path


NS = {
    "m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}


def read_ghia_xlsx(path: Path) -> tuple[list[tuple[float, float]], list[tuple[float, float]]]:
    """Return (y,u) and (x,v) Re=1000 point lists from the supplied workbook."""
    with zipfile.ZipFile(path) as book:
        names = set(book.namelist())
        strings: list[str] = []
        if "xl/sharedStrings.xml" in names:
            root = ET.fromstring(book.read("xl/sharedStrings.xml"))
            strings = [
                "".join(node.text or "" for node in item.findall(".//m:t", NS))
                for item in root.findall("m:si", NS)
            ]

        workbook = ET.fromstring(book.read("xl/workbook.xml"))
        relationships = ET.fromstring(book.read("xl/_rels/workbook.xml.rels"))
        rel_targets = {item.attrib["Id"]: item.attrib["Target"] for item in relationships}

        def value(cell: ET.Element | None):
            if cell is None:
                return None
            raw = cell.find("m:v", NS)
            if cell.attrib.get("t") == "inlineStr":
                return "".join(node.text or "" for node in cell.findall(".//m:t", NS))
            if raw is None:
                return None
            if cell.attrib.get("t") == "s":
                return strings[int(raw.text)]
            try:
                return float(raw.text)
            except (TypeError, ValueError):
                return raw.text

        for sheet in workbook.findall("m:sheets/m:sheet", NS):
            rel_id = sheet.attrib[f"{{{NS['r']}}}id"]
            target = rel_targets[rel_id]
            target = target.lstrip("/") if target.startswith("/") else f"xl/{target}"
            xml = ET.fromstring(book.read(target))
            rows = xml.findall(".//m:sheetData/m:row", NS)
            row_maps = {
                int(row.attrib["r"]): {
                    cell.attrib["r"].rstrip("0123456789"): value(cell)
                    for cell in row.findall("m:c", NS)
                }
                for row in rows
            }
            headers = [
                (row_number, row)
                for row_number, row in row_maps.items()
                if any("grid pt. no." == str(item).strip().lower() for item in row.values())
                and any(str(item).strip() == "Re=1000" for item in row.values())
            ]
            profiles = []
            for header_row, header in headers:
                re_col = next(col for col, item in header.items() if str(item).strip() == "Re=1000")
                coord_col = next(
                    col
                    for col, item in header.items()
                    if str(item).strip().lower() in {"x", "y"}
                )
                pairs = []
                for row_number in sorted(row_maps):
                    if row_number <= header_row:
                        continue
                    row = row_maps[row_number]
                    coord, velocity = row.get(coord_col), row.get(re_col)
                    if isinstance(coord, (int, float)) and isinstance(velocity, (int, float)):
                        pairs.append((float(coord), float(velocity)))
                    elif pairs:
                        break
                profiles.append((str(header[coord_col]).strip().lower(), pairs))
            if len(profiles) >= 2:
                by_coord = {name: data for name, data in profiles}
                if "y" in by_coord and "x" in by_coord:
                    return by_coord["y"], by_coord["x"]
    raise ValueError("Could not identify the Re=1000 x/y profile tables in the workbook")


def read_internal_vectors(path: Path, expected_count: int | None = None) -> list[tuple[float, float, float]]:
    text = path.read_text(encoding="utf-8", errors="replace")
    text = re.sub(r"/\*.*?\*/|//[^\n]*", "", text, flags=re.S)
    match = re.search(
        r"internalField\s+nonuniform\s+List<vector>\s+\d+\s*\((.*?)\)\s*;",
        text,
        flags=re.S,
    )
    if not match:
        uniform = re.search(
            r"internalField\s+uniform\s*\(\s*([-+0-9.eE]+)\s+([-+0-9.eE]+)\s+([-+0-9.eE]+)\s*\)",
            text,
        )
        if uniform and expected_count is not None:
            vector = tuple(float(component) for component in uniform.groups())
            return [vector] * expected_count
        raise ValueError(f"No supported ASCII vector internalField in {path}")
    values = re.findall(
        r"\(\s*([-+0-9.eE]+)\s+([-+0-9.eE]+)\s+([-+0-9.eE]+)\s*\)",
        match.group(1),
    )
    return [(float(x), float(y), float(z)) for x, y, z in values]


def time_directories(case: Path) -> list[tuple[float, Path]]:
    result = []
    for path in case.iterdir():
        try:
            time = float(path.name)
        except ValueError:
            continue
        if path.is_dir() and (path / "U").is_file():
            result.append((time, path))
    return sorted(result)


def build_grid(centres, velocities):
    if len(centres) != len(velocities):
        raise ValueError(f"C and U cell counts differ: {len(centres)} vs {len(velocities)}")
    # OpenFOAM writePrecision is six, so cell-centre coordinates are rounded
    # in the ASCII file; seven decimal places retain the 0.1/128 spacing.
    xs = sorted({round(c[0], 7) for c in centres})
    ys = sorted({round(c[1], 7) for c in centres})
    if len(xs) * len(ys) != len(centres):
        raise ValueError("Cell centres do not form a complete structured 2D grid")
    grid = [[None for _ in xs] for _ in ys]
    for centre, velocity in zip(centres, velocities):
        ix = min(range(len(xs)), key=lambda i: abs(xs[i] - centre[0]))
        iy = min(range(len(ys)), key=lambda i: abs(ys[i] - centre[1]))
        grid[iy][ix] = velocity
    if any(item is None for row in grid for item in row):
        raise ValueError("Could not map cell-centred fields onto x/y coordinates")
    return xs, ys, grid


def bracket(axis, target):
    if target <= axis[0]:
        return 0, 1
    if target >= axis[-1]:
        return len(axis) - 2, len(axis) - 1
    hi = next(i for i, x in enumerate(axis) if x >= target)
    return hi - 1, hi


def interpolate(xs, ys, grid, x, y, component):
    x0, x1 = bracket(xs, x)
    y0, y1 = bracket(ys, y)
    tx = (x - xs[x0]) / (xs[x1] - xs[x0])
    ty = (y - ys[y0]) / (ys[y1] - ys[y0])
    q00 = grid[y0][x0][component]
    q10 = grid[y0][x1][component]
    q01 = grid[y1][x0][component]
    q11 = grid[y1][x1][component]
    return (1 - ty) * ((1 - tx) * q00 + tx * q10) + ty * (
        (1 - tx) * q01 + tx * q11
    )


def write_csv(path, headers, rows):
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream)
        writer.writerow(headers)
        writer.writerows(rows)


def write_svg_plot(path, line_x, line_y, point_x, point_y, xlabel, ylabel, title):
    """Write a small dependency-free SVG line/point comparison plot."""
    width, height = 760, 590
    left, right, top, bottom = 92, 720, 58, 492
    all_x = list(line_x) + list(point_x)
    all_y = list(line_y) + list(point_y)
    xmin, xmax = min(all_x), max(all_x)
    ymin, ymax = min(all_y), max(all_y)
    xpad = max((xmax - xmin) * 0.06, 0.02)
    ypad = max((ymax - ymin) * 0.06, 0.02)
    xmin, xmax = xmin - xpad, xmax + xpad
    ymin, ymax = ymin - ypad, ymax + ypad
    sx = lambda x: left + (x - xmin) / (xmax - xmin) * (right - left)
    sy = lambda y: bottom - (y - ymin) / (ymax - ymin) * (bottom - top)
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
        '<style>text{font-family:Arial,sans-serif;fill:#222}.grid{stroke:#ddd;stroke-width:1}.axis{stroke:#333;stroke-width:1.4}.curve{fill:none;stroke:#1675b9;stroke-width:2.4}.ref{fill:#c43c39;stroke:white;stroke-width:1}</style>',
        f'<text x="{width/2}" y="28" text-anchor="middle" font-size="19">{title}</text>',
    ]
    for index in range(6):
        frac = index / 5
        xval = xmin + frac * (xmax - xmin)
        xpos = sx(xval)
        yval = ymin + frac * (ymax - ymin)
        ypos = sy(yval)
        parts.append(f'<line class="grid" x1="{xpos:.2f}" y1="{top}" x2="{xpos:.2f}" y2="{bottom}"/>')
        parts.append(f'<text x="{xpos:.2f}" y="{bottom+22}" text-anchor="middle" font-size="12">{xval:.3g}</text>')
        parts.append(f'<line class="grid" x1="{left}" y1="{ypos:.2f}" x2="{right}" y2="{ypos:.2f}"/>')
        parts.append(f'<text x="{left-10}" y="{ypos+4:.2f}" text-anchor="end" font-size="12">{yval:.3g}</text>')
    parts.extend([
        f'<line class="axis" x1="{left}" y1="{bottom}" x2="{right}" y2="{bottom}"/>',
        f'<line class="axis" x1="{left}" y1="{top}" x2="{left}" y2="{bottom}"/>',
        f'<text x="{(left+right)/2}" y="{height-35}" text-anchor="middle" font-size="15">{xlabel}</text>',
        f'<text x="24" y="{(top+bottom)/2}" text-anchor="middle" font-size="15" transform="rotate(-90 24 {(top+bottom)/2})">{ylabel}</text>',
    ])
    points = " ".join(f"{sx(x):.2f},{sy(y):.2f}" for x, y in zip(line_x, line_y))
    parts.append(f'<polyline class="curve" points="{points}"/>')
    for x, y in zip(point_x, point_y):
        parts.append(f'<circle class="ref" cx="{sx(x):.2f}" cy="{sy(y):.2f}" r="4.5"/>')
    parts.extend([
        '<line class="curve" x1="470" y1="535" x2="510" y2="535"/>',
        '<text x="518" y="540" font-size="13">OpenFOAM Re=1000</text>',
        '<circle class="ref" cx="665" cy="535" r="4.5"/>',
        '<text x="677" y="540" font-size="13">Ghia et al. (1982)</text>',
        '</svg>',
    ])
    path.write_text("\n".join(parts), encoding="utf-8")


def main():
    # Retain the historic Re=1000 entry point, but delegate to the parameterized
    # analyzer that uses prescribed cavity values at wall endpoints.
    import runpy
    import sys

    migration_dir = Path(__file__).resolve().parents[1]
    generic_analyzer = migration_dir / "cfd-cavity-validation" / "scripts" / "analyze_cavity.py"
    ghia_workbook = (
        migration_dir
        / "cfd-cavity-validation"
        / "reference-data"
        / "Ghia_et_al_1982_data.xlsx"
    )
    defaults = [
        "--re", "1000",
        "--case", str(Path(__file__).resolve().parent / "case"),
        "--ghia", str(ghia_workbook),
        "--out", str(migration_dir / "cfd-cavity-validation" / "re1000" / "results"),
        "--delta-t", "0.0002",
        "--cell-count", "128",
        "--precision", "7",
    ]
    sys.argv = [str(generic_analyzer), *defaults, *sys.argv[1:]]
    runpy.run_path(str(generic_analyzer), run_name="__main__")
    return

    parser = argparse.ArgumentParser()
    parser.add_argument("--case", type=Path, required=True)
    parser.add_argument("--ghia", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    ghia_u, ghia_v = read_ghia_xlsx(args.ghia)
    times = time_directories(args.case)
    if not times:
        raise ValueError("No saved U time directories found")
    latest_time, latest_dir = times[-1]
    centres_path = latest_dir / "C"
    if not centres_path.is_file():
        raise FileNotFoundError(
            f"Cell-centre field missing at {centres_path}; run foamPostProcess -func writeCellCentres"
        )
    centres = read_internal_vectors(centres_path, 128 * 128)
    if len(centres) != 128 * 128:
        raise ValueError(f"Expected 16384 cell centres, got {len(centres)}")

    snapshots = {}
    for time, directory in times:
        vectors = read_internal_vectors(directory / "U", len(centres))
        if len(vectors) != len(centres):
            raise ValueError(f"Unexpected U count at t={time}: {len(vectors)}")
        snapshots[time] = vectors

    monitor_delta = 0.1
    monitor_rows = []
    thresholds = {1e-3: None, 1e-4: None, 1e-5: None}
    times_by_value = {round(t, 8): t for t in snapshots}
    for time, directory in times:
        previous = times_by_value.get(round(time - monitor_delta, 8))
        if previous is None:
            continue
        now = snapshots[time]
        before = snapshots[previous]
        numerator = sum(
            (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2
            for a, b in zip(now, before)
        )
        denominator = sum(a[0] ** 2 + a[1] ** 2 + a[2] ** 2 for a in now)
        epsilon = math.sqrt(numerator / denominator) if denominator else math.inf
        xs, ys, grid = build_grid(centres, now)
        reps = [
            ("center", 0.05, 0.05),
            ("upper", 0.05, 0.075),
            ("lower", 0.05, 0.025),
            ("left", 0.025, 0.05),
            ("right", 0.075, 0.05),
        ]
        velocities = [
            (name, interpolate(xs, ys, grid, x, y, 0), interpolate(xs, ys, grid, x, y, 1))
            for name, x, y in reps
        ]
        monitor_rows.append(
            [time, time * 10, round(time / 0.0002), epsilon]
            + [component for _, u, v in velocities for component in (u, v)]
        )
        for threshold in thresholds:
            if epsilon < threshold and thresholds[threshold] is None:
                thresholds[threshold] = time

    write_csv(
        args.out / "steady_metrics.csv",
        ["t_s", "t_star", "steps", "epsilon_U"]
        + [f"{name}_{component}" for name in ("center", "upper", "lower", "left", "right") for component in ("u", "v")],
        monitor_rows,
    )

    xs, ys, grid = build_grid(centres, snapshots[latest_time])
    # Ghia coordinates are dimensionless; convert them to the 0.1 m case domain.
    of_u = [(coord, interpolate(xs, ys, grid, 0.05, coord * 0.1, 0)) for coord, _ in ghia_u]
    of_v = [(coord, interpolate(xs, ys, grid, coord * 0.1, 0.05, 1)) for coord, _ in ghia_v]
    comparison_rows = []
    for (coord, ref), (_, calc) in zip(ghia_u, of_u):
        comparison_rows.append(["u_vs_y", coord, ref, calc, abs(ref - calc)])
    for (coord, ref), (_, calc) in zip(ghia_v, of_v):
        comparison_rows.append(["v_vs_x", coord, ref, calc, abs(ref - calc)])
    write_csv(args.out / "centerline_comparison.csv", ["profile", "coordinate", "ghia", "openfoam", "abs_error"], comparison_rows)

    def report_errors(profile, pairs):
        errors = [abs(reference - calculation) for _, reference, calculation in pairs]
        rmse = math.sqrt(
            sum((reference - calculation) ** 2 for _, reference, calculation in pairs)
            / len(pairs)
        )
        worst = max(range(len(errors)), key=errors.__getitem__)
        print(
            f"{profile}: n={len(errors)} maxAE={errors[worst]:.8g} "
            f"MAE={sum(errors)/len(errors):.8g} RMSE={rmse:.8g} "
            f"worst_coordinate={pairs[worst][0]:.8g}"
        )

    report_errors(
        "vertical u(y)",
        [(coord, ref, calc) for (coord, ref), (_, calc) in zip(ghia_u, of_u)],
    )
    report_errors(
        "horizontal v(x)",
        [(coord, ref, calc) for (coord, ref), (_, calc) in zip(ghia_v, of_v)],
    )
    print("latest time:", latest_time, "t*:", latest_time * 10)
    print("threshold first crossings:", thresholds)
    print("centerline interpolation: bilinear on cell-centred C coordinates, linear extrapolation to wall endpoints")

    write_svg_plot(
        args.out / "u_centerline_re1000.svg",
        [y for y, _ in of_u], [u for _, u in of_u],
        [y for y, _ in ghia_u], [u for _, u in ghia_u],
        "y / L", "u / U_lid", "Vertical centerline velocity",
    )
    write_svg_plot(
        args.out / "v_centerline_re1000.svg",
        [x for x, _ in of_v], [v for _, v in of_v],
        [x for x, _ in ghia_v], [v for x, v in ghia_v],
        "x / L", "v / U_lid", "Horizontal centerline velocity",
    )


if __name__ == "__main__":
    main()
