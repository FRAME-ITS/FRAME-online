[![Build Status](https://github.com/FRAME-ITS/FRAME-online/actions/workflows/ci.yml/badge.svg)](https://github.com/FRAME-ITS/FRAME-online/actions/workflows/ci.yml)
[![GitHub Pages](https://img.shields.io/badge/Pages-deployed-brightgreen)](https://frame-its.github.io/FRAME-online/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

# FRAME Website

This repository contains the source code for the **FRAME online website**, presenting the FRAME methodology (*FRamework Architecture Made for Europe*) and all resources.

---

## 📁 Repository Structure

- **`/docs`** — All website content (Markdown pages, images, navigation structure).  
- **`mkdocs.yml`** — MkDocs configuration file.  
- **`pdm.lock` / `pyproject.toml`** — Python project and dependency management via PDM.

---

## 🛠️ Local Installation

The project uses **Python 3.12** and **PDM** for environment and dependency management.

```bash
pdm install
```

Before running MkDocs, activate the virtual environment created by PDM:

```bash
pdm venv activate
```

---

## 🧪 Local Development

Edit Markdown files inside the `docs` folder.  
MkDocs documentation: https://www.mkdocs.org/user-guide/writing-your-docs/

Start a local development server from the project root:

```bash
mkdocs serve
```

Then open:

```
http://localhost:8000
```

The site will automatically reload whenever you save changes.

---

## 🚀 Deployment (GitHub Pages)

Deployment is fully automated.  
Simply push changes to the repository — GitHub Actions will build and publish the site to GitHub Pages.

---

## 🙏 Acknowledgement

<img src="docs/assets/img/cofinanced-eu-logo.png" alt="Co-financed by European Union" width="50%" height="auto" align="right">

The FRAME has received funding from the European Union's Connecting Europe Facility (CEF) programme under grant agreement No [MOVE/C3/SUB/2016-405/CEF/PSA/SI2.759934]. For more information go to Projects section.

The content of this document reflects only the authors' views, and the European Union is not responsible for any use that may be made of the information it contains.

