# IJSCAR Publishing Workflow

Step-by-step guide for assembling and publishing a new issue from accepted manuscripts to live website.

---

## Overview

A finished issue requires these components, in order:

1. Cover page (PDF)
2. Editor-in-Chief letter (PDF)
3. Table of contents / index page (PDF)
4. Individual article PDFs (compiled from author LaTeX)
5. Merged issue PDF (`volN-issueN.pdf`)
6. Individual article HTML pages on ijscar.org/pubs/
7. DOIs registered with Crossref

---

## Step 1 — Collect Final Author PDFs

- Ask each author for their **final compiled PDF** (or compile from their LaTeX zip yourself via Overleaf).
- Confirm the first page shows: two-column ACM format, line numbers, CC BY 4.0 license block in the bottom-left footer, and the correct conference/volume/issue/year metadata.
- Rename each PDF clearly, e.g. `01_punuru.pdf`, `02_omar.pdf`, etc., numbered in publication order.
- Place them in `pubs/papers/vol<N>-issue<N>/`.

---

## Step 2 — Create the Cover Page

- Design in Canva, Adobe InDesign, or Google Slides.
- Must include: IJSCAR logo, volume number, issue number, month and year, ISSN.
- Export as a single-page PDF: `pubs/components/vol<N>-issue<N>/cover.pdf`

---

## Step 3 — Write the Editor-in-Chief Letter

- Write in Google Docs or Word, then export to PDF.
- Typical content: welcome note, brief description of each article, acknowledgments.
- Save as: `pubs/components/vol<N>-issue<N>/editor-letter.pdf`

---

## Step 4 — Create the Table of Contents Page

- List all articles in publication order with author names and page ranges.
- Page ranges must be finalized before this step (count pages in each article PDF).
- Export as PDF: `pubs/components/vol<N>-issue<N>/toc.pdf`

---

## Step 5 — Merge All Components into One Issue PDF

Install `pypdf` if you haven't already:

```bash
pip install pypdf
```

Edit `merge_issue.py` (in the `pubs/` directory) with the correct volume, issue, and file paths, then run:

```bash
cd pubs
python3 merge_issue.py
```

The script (`pubs/merge_issue.py`):

```python
#!/usr/bin/env python3
"""Merge all components of an IJSCAR issue into a single PDF."""

from pypdf import PdfWriter

# ── Configuration — update these for each new issue ───────────────────────────
VOLUME = 3
ISSUE  = 2
OUTPUT = f"vol{VOLUME}-issue{ISSUE}.pdf"

# List PDFs in the order they should appear in the final issue.
# Paths are relative to pubs/.
COMPONENTS = [
    "components/vol3-issue2/cover.pdf",
    "components/vol3-issue2/editor-letter.pdf",
    "components/vol3-issue2/toc.pdf",
    "papers/vol3-issue2/01_punuru.pdf",
    "papers/vol3-issue2/02_omar.pdf",
    "papers/vol3-issue2/03_goel.pdf",
    "papers/vol3-issue2/04_mehra.pdf",
    "papers/vol3-issue2/05_raghavan.pdf",
]
# ──────────────────────────────────────────────────────────────────────────────

writer = PdfWriter()

for path in COMPONENTS:
    writer.append(path)
    print(f"  added: {path}")

with open(OUTPUT, "wb") as f:
    writer.write(f)

print(f"\nDone — wrote {OUTPUT}")
```

Move the output PDF to the correct location in the repo:

```bash
mv vol3-issue2.pdf /Users/mariahwang/Github/Ijscar/pubs/vol3-issue2.pdf
```

---

## Step 6 — Record Page Numbers and Update articles.csv

Now that the issue PDF is assembled, count the page ranges for each article and fill them into `pubs/articles.csv`.

Open `articles.csv` and fill in `page_start` and `page_end` for each new article row. Pages refer to the page number **within the merged PDF file** (not the printed number on the paper).

Then regenerate the individual article HTML pages:

```bash
cd /Users/mariahwang/Github/Ijscar/pubs
python3 generate_article_pages.py
```

---

## Step 7 — Register DOIs with Crossref

1. Log in to Crossref at [doi.crossref.org](https://doi.crossref.org).
2. Prepare the metadata XML deposit (or use the web form) for each article.
3. Each article needs: title, authors, affiliations, abstract, volume, issue, year, page range, ISSN, and the URL of its individual article page on ijscar.org (e.g. `https://ijscar.org/pubs/articles/vol3-issue2-punuru-drone-navigation`).
4. Submit the deposit. DOIs are typically activated within a few hours.

---

## Step 8 — Add DOIs to articles.csv and Regenerate Pages

Once Crossref confirms the DOIs, fill in the `doi` column in `pubs/articles.csv` for each new article (format: `https://doi.org/10.XXXXX/...`).

Then regenerate again:

```bash
cd /Users/mariahwang/Github/Ijscar/pubs
python3 generate_article_pages.py
```

---

## Step 9 — Commit Everything to GitHub

```bash
cd /Users/mariahwang/Github/Ijscar
git add pubs/vol3-issue2.pdf pubs/articles.csv pubs/articles/ pubs/index.md
git commit -m "publish Vol. 3 Issue 2"
git push
```

GitHub Pages will rebuild automatically. Allow 1–2 minutes, then verify at [ijscar.org/pubs](https://ijscar.org/pubs).

---

## Quick Reference — Files to Update for Each New Issue

| File | What to update |
|---|---|
| `pubs/articles.csv` | Add one row per article; fill pages and DOI once known |
| `pubs/index.md` | Add new `### Volume N, Issue N` section with article links |
| `pubs/generate_article_pages.py` | Add entry to `ISSUE_PDF` dict; add slug overrides if needed |
| `pubs/merge_issue.py` | Update `VOLUME`, `ISSUE`, and `COMPONENTS` list |
| `pubs/volN-issueN.pdf` | The merged issue PDF itself |
