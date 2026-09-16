# CFD教材 Phase 2B: Word/PDF → MyST Markdown移植

調査・移植日: 2026-09-16

## Source files

- `数値流体解析演習_blueCFD2024編.docx`：段落、表、画像、OMML数式の主ソース。
- `数値流体解析演習_blueCFD2024編.pdf`：42ページのレイアウト、図配置、キャプション、章境界の照合用。
- `migration/cfd-materials-inventory.md`：Phase 1で確定した構造、provenance、未解決事項。

DOCXはPandoc 3.10で一時変換し、PDFの42ページ構成と照合した。DOCX/PDF本体は変更していない。

## Conversion method

Pandocによる初期Markdown化と`--extract-media`での画像抽出を行い、最終MarkdownはMySTの見出し、code block、directiveへ手動で整理した。DOCXの表から得たOpenFOAM dictionaryはMarkdown tableではなく、必要な部分をfenced code blockへ移した。OMMLのCourant数式とReynolds数の説明はLaTeX形式へ正規化した。

## Chapter mapping

| MyST file | Source pages | Phase 2B status |
| --- | --- | --- |
| `bluecfd-install.md` | pp.1--4 | 初期移植完了 |
| `cavity.md` | pp.1、5--13 | 初期移植完了 |
| `cavity-settings.md` | pp.14--23 | 初期移植完了 |
| `blockmesh-boundary.md` | pp.24--31 | 初期移植完了 |
| `external-flow-2d.md` | pp.32--34 | 見出し・課題の初期配置 |
| `external-flow-3d.md` | pp.35--39 | 見出し・手順の初期配置 |
| `external-flow-3d-custom.md` | pp.40--42 | 見出し・手順の初期配置 |

授業回を示す「前回」「今回」「次回」は、章名や節名を参照する表現へ置き換えた。

## Figures migrated

Phase 2Bでは、教員作成の説明図、OpenFOAM/ParaViewの解析結果、操作手順の理解に必要な一部のスクリーンショットを、意味のある英語名へ変更して`textbook/cfd/images/`へ配置した。`image32.png`/`image33.png`の重複は一つに統合した。

移行した主な画像は次のとおりである。

- blueCFD terminal初回画面
- cavityの目標画面、圧力場、速度ベクトル
- cavityとchannelの概念比較
- channel境界条件
- square-cylinderのblock、mesh、圧力、速度、vorticityの説明図

## Figures withheld / replaced

- Ghia et al. (1982)の原図2点は転載せず、`cavity-settings.md`に自作再計算図へのplaceholderを置いた。
- 学生作成図は公開許諾が未確認のため掲載していない。
- Sketchfab由来の車両画像、出典不明の3D結果図は、今回のMySTには掲載していない。
- 古いParaView UIを含む図は、2026環境で再撮影するまで主要手順の根拠にしない。

## Equations converted

- `Re = UL/nu`
- `C = U Delta t / Delta x`
- `nu = UL/Re_target`

数式は画像化せず、MySTのinline/display mathとして記述した。

## Legacy commands updated

- 旧資料の`icoFoam`実行は、2026年版の標準手順では`foamRun`へ更新した。
- 旧`channel_2024.tgz`、`vehicle_2025.tgz`の展開手順は、`OpenFOAM-exercises v2026.1` Release Assetへのリンクへ置き換えた。
- 渦度の後処理は`postProcess -func vorticity`を主経路とし、単独の`vorticity`はlegacy情報として区別した。
- 現行cavityの設定ファイル名として`physicalProperties`、`momentumTransport`、`controlDict`、`blockMeshDict`を示した。

## OpenFOAM 12 changes

現在のcase repositoryを参照し、cavityとchannelは`foamRun` / `incompressibleFluid`、層流設定は`constant/momentumTransport`を使う形で説明した。cavityの初期値は`nu=0.01`、`U=1`、`L=0.1`、`Re=10`として記載した。vehicleはRelease Assetの`Allrun`を使う手順へ整理した。

## Release links added

caseを使う章から次のReleaseページへリンクした。

<https://github.com/Kogakuin-FEL/OpenFOAM-exercises/releases/tag/v2026.1>

学生用ファイルは`OpenFOAM-exercises-2026.1.zip`であり、GitHub自動生成の`Source code (zip)`ではないことを明記した。

## Unresolved issues

- Ghia benchmarkの自作再計算図は未作成。
- `square-cylinder` caseは`v2026.1`に含まれていない。
- 学生作成画像の公開許諾・匿名化・クレジットは未確定。
- 出典不明の3D画像は掲載保留。
- blueCFD-Core、ParaView、Windows UIスクリーンショットは将来の対象環境で再撮影する余地がある。
- 後半3章は初期移植であり、図版・詳細なcase説明・課題導線の完全統合はPhase 2B後半で行う。
- WSL/Linux/macOS、standalone ParaView、Notepad2などの補足は、主経路と重複しない形への最終整理が必要。
