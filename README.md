# FRAME Website

[![Build Status](https://github.com/FRAME-ITS/FRAME-online/actions/workflows/ci.yml/badge.svg)](https://github.com/FRAME-ITS/FRAME-online/actions/workflows/ci.yml)
[![GitHub Pages](https://img.shields.io/badge/Pages-deployed-brightgreen)](https://frame-its.github.io/FRAME-online/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

This repository contains the source code for the **FRAME online website**, presenting the FRAME methodology (*FRamework Architecture Made for Europe*) and all resources.

## 📁 Repository Structure

- **`/docs`** — All website content (Markdown pages, images, navigation structure).  
- **`mkdocs.yml`** — MkDocs configuration file.  
- **`pyproject.toml`** — Python dependencies (Zensical).

## 🛠️ Local Installation

The website is built with [Zensical](https://zensical.org) (successor of Material for MkDocs; it reads `mkdocs.yml`). Any Python 3.10 or later works.

```bash
python -m venv .venv
.venv/bin/python -m pip install zensical        # Windows: .\.venv\Scripts\python -m pip install zensical
```

---

## 🧪 Local Development

Edit Markdown files inside the `docs` folder and start a local server from the project root:

```bash
.venv/bin/zensical serve                         # Windows: .\.venv\Scripts\zensical serve
```

Then open the address printed in the console (http://localhost:8000/FRAME-online/). The site reloads whenever you save changes.

---

## 🚀 Deployment (GitHub Pages)

Deployment is fully automated.  
Merge changes into `main` — GitHub Actions (`.github/workflows/ci.yml`) builds the site with Zensical and publishes it to GitHub Pages.

## 🙏 Acknowledgement

<img src="docs/assets/img/cofinanced-eu-logo.png" alt="Co-financed by European Union" width="50%" height="auto" align="right">

The FRAME has received funding from the European Union's Connecting Europe Facility (CEF) programme under grant agreement No [MOVE/C3/SUB/2016-405/CEF/PSA/SI2.759934]. For more information go to Projects section.

The content of this document reflects only the authors' views, and the European Union is not responsible for any use that may be made of the information it contains.

