# FluidSeminarMaterials

Teaching and learning materials for the **Fluid Engineering Seminar**,  
Department of Mechanical Engineering, **Kogakuin University**.

---

## Overview

This repository contains course materials used in the *Fluid Engineering Seminar* at Kogakuin University.  
The contents are written in **Japanese**, as they are intended for use in classes conducted in Japan.

The online textbook is built from [`textbook/`](textbook/) and published with GitHub Pages. It covers three main areas:

- **Python / JupyterLab programming**, including PyGame-CE lessons
- **UNIX / Linux / WSL operation**, including UBX exercises
- **CFD / OpenFOAM**, including simulations with blueCFD-Core and visualization with ParaView


📘 **Online Textbook (GitHub Pages)**  
The Jupyter Book version of these materials is available here:  
👉 [https://akonno.github.io/FluidSeminarMaterials/](https://akonno.github.io/FluidSeminarMaterials/)

Student-facing materials, including the Conda environment, Jupyter notebooks, small exercise datasets, and PyGame files, are grouped in [`student/`](student/). The [`student/environment.yml`](student/environment.yml) file is for learner Python/JupyterLab exercises, not for building the textbook. GitHub Actions builds the Jupyter Book with Python 3.14 and Jupyter Book 2.1.6; local Linux builds use the separate `textbook-build` environment. Larger, versioned CFD case packages may be distributed separately, for example through a dedicated repository or GitHub Release assets.

The [`authoring/`](authoring/) directory contains maintainer tools and examples for preparing course materials.


---

## Description

> Japanese-language teaching materials for the Fluid Engineering Seminar, covering Python/JupyterLab programming, UNIX/Linux/WSL operation, and CFD/OpenFOAM.

---

## License

The repository contains two categories of content governed by different licenses:

| Type | License | Description |
|------|----------|-------------|
| **Educational materials** (text, figures, and MyST/Markdown documents) | [Creative Commons BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) | May be shared and adapted for non-commercial educational use with attribution and share-alike terms. Some screenshots and third-party UI images are excluded; see [LICENSE-docs.md](LICENSE-docs.md) for details. |
| **Source code and executable examples** (Python, notebook cells, and scripts) | [MIT License](LICENSE) | Freely usable, modifiable, and redistributable under the terms of the MIT License. |


---

## Author / Maintainer

Akihisa Konno  
Department of Mechanical Engineering, Kogakuin University  
Tokyo, Japan
