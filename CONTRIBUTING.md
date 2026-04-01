# Contributing to FRAME‑online

Thank you for your interest in contributing to the **FRAME online website**.  
This repository hosts the MkDocs‑based documentation site for the FRAME methodology (*FRamework Architecture Made for Europe*).  
Contributions that improve clarity, structure, correctness, or usability are welcome.

---

## 🧭 How to Contribute

### 1. Fork the repository
Create your own fork and clone it locally:

```bash
git clone https://github.com/<your-username>/FRAME-online.git
cd FRAME-online
```

### 2. Set up the development environment

The project uses **Python 3.12** and **PDM**.

```bash
pdm install
pdm venv activate
```

Verify MkDocs is available:

```bash
mkdocs --version
```

### 3. Run the local development server

```bash
mkdocs serve
```

Open:

```
http://localhost:8000
```

The site reloads automatically when you edit files in `docs/`.

---

## 📁 Project Structure

- `docs/` — Markdown content, images, navigation structure  
- `mkdocs.yml` — MkDocs configuration  
- `pyproject.toml` — dependencies and PDM configuration  

Please keep content modular and consistent with the existing structure.

---

## ✍️ Writing Guidelines

To maintain consistency across the site:

- Use **Markdown** (`.md`) for all content.
- Prefer **short, clear sections** with meaningful headings.
- Use **relative links** (`../folder/page.md`) within the docs.
- Keep filenames **lowercase-with-hyphens**.
- Avoid marketing language; focus on clarity and technical accuracy.
- When adding diagrams or images, place them in `docs/assets/`.

---

## 🔍 Style and Quality Checks

Before submitting:

- Ensure the site builds without warnings:

  ```bash
  mkdocs build
  ```

- Check internal links.
- Validate that navigation remains coherent.
- Keep commit messages descriptive and atomic.

---

## 🔀 Pull Requests

When opening a PR:

1. Describe **what** you changed and **why**.  
2. Reference related issues if applicable.  
3. Keep PRs focused—small, reviewable changes are preferred.  
4. Ensure the site builds successfully.

All contributions are reviewed for technical accuracy, consistency, and alignment with FRAME methodology.

---

## 🧩 Issues and Feature Requests

If you find a bug, inconsistency, or missing content:

- Open an issue with a clear description.
- Include steps to reproduce (if relevant).
- Suggest improvements when possible.

---

## 📜 License

By contributing, you agree that your contributions will be licensed under the repository’s license (MIT unless changed).
