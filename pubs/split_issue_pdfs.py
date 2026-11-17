#!/usr/bin/env python3
"""Cut per-article PDFs out of a merged issue PDF.

Google Scholar can't index several papers inside one PDF and ignores files
over 5 MB, so each article needs its own small PDF at
pubs/articles/<slug>.pdf (the slug is the article page's file name).

Usage (from pubs/):
    python3 split_issue_pdfs.py 2.1 3.1        # volume.issue, one or more
    python3 split_issue_pdfs.py 2.1 --dry-run  # show what would be written

For each article the script
  * finds the PDF page where the article starts by looking for its title near
    the top of a page (skipping the contents page), rather than trusting
    page_start in articles.csv, which is off by one for some older issues;
  * writes pages [start, next article's start) to articles/<slug>.pdf;
  * downsamples images only if the result is over 4.5 MB (needs `pymupdf`);
  * adds `citation_pdf:` to the article's front matter if it is missing.

Requires: pypdf  (and pymupdf only when a file needs shrinking).
"""

import csv
import os
import re
import sys

from pypdf import PdfReader, PdfWriter

HERE = os.path.dirname(os.path.abspath(__file__))
ARTICLES_DIR = os.path.join(HERE, "articles")
MAX_BYTES = int(4.5 * 1024 * 1024)  # stay clear of Scholar's 5 MB limit


def norm(text):
    return re.sub(r"[^a-z0-9]+", "", text.lower())


def slugify(text):
    text = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"[\s_]+", "-", text).strip("-")


def find_slug(vol, iss, last):
    prefix = f"vol{vol}-issue{iss}-{slugify(last)}-"
    matches = [f[:-3] for f in os.listdir(ARTICLES_DIR)
               if f.startswith(prefix) and f.endswith(".md")]
    if len(matches) != 1:
        raise SystemExit(f"expected one page for {prefix}*, found {matches}")
    return matches[0]


def find_starts(reader, rows):
    """1-based start page of each article, in the same order as rows."""
    texts = [(p.extract_text() or "") for p in reader.pages]
    starts = []
    for row in rows:
        key = norm(row["article_title"])[:45]
        hit = None
        for idx, text in enumerate(texts):
            if "contents" in text.lower()[:300]:
                continue  # the issue's table-of-contents page also has titles
            if key in norm(text)[:900]:
                hit = idx + 1
                break
        if hit is None:
            raise SystemExit(f"could not find the first page of: {row['article_title']}")
        starts.append(hit)
    return starts


def shrink(path):
    import pymupdf  # only needed for the occasional image-heavy article

    doc = pymupdf.open(path)
    doc.rewrite_images(dpi_threshold=170, dpi_target=150, quality=85,
                       lossy=True, lossless=True)
    tmp = path + ".tmp"
    doc.save(tmp, garbage=4, deflate=True, clean=True)
    doc.close()
    os.replace(tmp, path)


def add_front_matter_pdf(slug):
    md_path = os.path.join(ARTICLES_DIR, f"{slug}.md")
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    if re.search(r"^citation_pdf:", text, re.M):
        return False
    line = f'citation_pdf: "/pubs/articles/{slug}.pdf"\n'
    # front matter is the block between the first two '---' lines
    head, sep, rest = text.partition("\n---\n")
    if not text.startswith("---\n") or not sep:
        raise SystemExit(f"{md_path} has no front matter")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(head + "\n" + line.rstrip("\n") + sep + rest)
    return True


def main(argv):
    dry = "--dry-run" in argv
    issues = [a for a in argv if not a.startswith("--")]
    if not issues:
        raise SystemExit(__doc__)

    with open(os.path.join(HERE, "articles.csv"), newline="", encoding="utf-8") as f:
        all_rows = list(csv.DictReader(f))

    for spec in issues:
        vol, iss = spec.split(".")
        rows = [r for r in all_rows if r["volume"] == vol and r["issue"] == iss]
        reader = PdfReader(os.path.join(HERE, f"vol{vol}-issue{iss}.pdf"))
        starts = find_starts(reader, rows)
        order = sorted(range(len(rows)), key=lambda k: starts[k])
        for pos, k in enumerate(order):
            first = starts[k]
            last = starts[order[pos + 1]] - 1 if pos + 1 < len(order) else len(reader.pages)
            slug = find_slug(vol, iss, rows[k]["author_Last"])
            out = os.path.join(ARTICLES_DIR, f"{slug}.pdf")
            print(f"vol{vol}-issue{iss} pp.{first}-{last} -> articles/{slug}.pdf")
            if dry:
                continue
            writer = PdfWriter()
            for page in range(first - 1, last):
                writer.add_page(reader.pages[page])
            with open(out, "wb") as fh:
                writer.write(fh)
            if os.path.getsize(out) > MAX_BYTES:
                shrink(out)
            size = os.path.getsize(out) / 1048576
            print(f"    {size:.2f} MB" + ("  (still over 4.5 MB!)" if size * 1048576 > MAX_BYTES else ""))
            if add_front_matter_pdf(slug):
                print("    added citation_pdf to front matter")


if __name__ == "__main__":
    main(sys.argv[1:])
