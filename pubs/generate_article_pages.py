#!/usr/bin/env python3
"""Generate individual Jekyll article pages from articles.csv."""

import csv
import os
import re

ARTICLES_CSV = os.path.join(os.path.dirname(__file__), "articles.csv")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "articles")

ISSUE_PDF = {
    (1, 1): "../vol1-issue1.pdf",
    (2, 1): "../vol2-issue1.pdf",
    (2, 2): "../vol2-issue2.pdf",
    (3, 1): "../vol3-issue1.pdf",
}


def slugify(text):
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text).strip("-")
    return text


def parse_more_authors(raw):
    """'Last, First | Last2, First2' → ['First Last', 'First2 Last2']"""
    if not raw or not raw.strip():
        return []
    result = []
    for entry in raw.split("|"):
        entry = entry.strip()
        if not entry:
            continue
        if "," in entry:
            last, first = entry.split(",", 1)
            result.append(f"{first.strip()} {last.strip()}")
        else:
            result.append(entry)
    return result


def format_authors_line(row):
    primary = f"{row['author_First']} {row['author_Last']}"
    others = parse_more_authors(row.get("more_authors_last_first", ""))
    all_authors = [primary] + others
    return ", ".join(all_authors)


def make_page(row):
    vol = int(row["volume"])
    iss = int(row["issue"])
    year = row["year"]
    title = row["article_title"]
    affiliation = row["affiliations"].strip()
    abstract = row["abstract"].strip()
    keywords = row["keywords"].strip()
    p_start = row["page_start"].strip()
    p_end = row["page_end"].strip()
    doi = row["doi"].strip()
    pdf_path = ISSUE_PDF.get((vol, iss), "../pubs/") + f"#page={p_start}"

    authors_line = format_authors_line(row)

    doi_display = doi.replace("https://doi.org/", "") if doi.startswith("https://doi.org/") else doi
    doi_section = f'**DOI:** [{doi_display}]({doi})' if doi else ""

    affiliation_section = f"**Affiliation:** {affiliation}" if affiliation else ""

    page = f"""---
layout: default
title: "{title.replace('"', '&quot;')}"
description: "{authors_line} — IJSCAR Vol. {vol}, Issue {iss}, {year}, pp. {p_start}–{p_end}"
---

# {title}

{authors_line}

{affiliation_section}

**IJSCAR** Vol. {vol}, Issue {iss} ({year}) &nbsp;·&nbsp; pp. {p_start}–{p_end}

{doi_section}

---

## Abstract

{abstract}

---

**Keywords:** {keywords}

---

[View Full Issue PDF]({pdf_path}){{: .button}} &nbsp; [All Publications](../)
"""
    return page.strip() + "\n"


STOPWORDS = {
    "a", "an", "the", "and", "or", "but", "of", "in", "on", "at", "to",
    "for", "with", "by", "from", "as", "is", "its", "it", "that", "this",
    "using", "based", "how", "their", "our", "we", "via", "into", "through",
    "study", "case", "approach", "analysis", "framework", "model", "method",
    "towards", "against", "use", "used", "uses", "understanding", "comparing",
    "leveraging", "enhancing", "streamlining", "predicting", "detecting",
    # generic ML/AI terms to avoid since almost every article uses them
    "machine", "learning", "deep", "artificial", "intelligence", "neural",
    "network", "networks", "performance", "traditional", "comparative",
    "hybrid", "automated", "automatic", "classification", "detection",
    "prediction", "modeling", "models", "algorithm", "algorithms",
    "data", "dataset", "results", "system", "systems", "code", "generation",
    "large", "language", "llm", "llms", "ai", "ml",
}

# Manual overrides for slugs where auto-extraction still produces vague results.
# Key: (volume, issue, author_last_lowercase)  Value: keyword suffix to use
SLUG_OVERRIDES = {
    ("1", "1", "zhang"):       "midi",
    ("1", "1", "pallapothu"):  "cardiac-mri",
    ("1", "1", "wang"):        "sonic-pi",
    ("1", "1", "amarnath"):    "infrastructure-as-code",
    ("2", "1", "hwang"):       "glaucoma-detection",
    ("2", "1", "maganti"):     "heat-pollution",
    ("2", "1", "raghav"):      "verilog",
    ("2", "1", "carvalho"):    "cloud-seeding",
    ("3", "1", "ranjit"):      "breast-cancer-survival",
    ("3", "1", "mkrtumyan"):   "phishing-imbalanced",
    ("3", "1", "sanku"):       "disaster-path-planning",
    ("3", "1", "cheng"):       "epta-zinc-docking",
}


def title_keywords(title, n=2):
    words = re.sub(r"[^\w\s]", " ", title).split()
    keywords = [w for w in words if w.lower() not in STOPWORDS and len(w) > 2]
    return "-".join(slugify(w) for w in keywords[:n])


def make_slug(row):
    vol = row["volume"]
    iss = row["issue"]
    last = slugify(row["author_Last"])
    key = (vol, iss, last)
    kw = SLUG_OVERRIDES.get(key) or title_keywords(row["article_title"])
    return f"vol{vol}-issue{iss}-{last}-{kw}"


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(ARTICLES_CSV, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    slug_counts = {}
    for row in rows:
        slug = make_slug(row)
        slug_counts[slug] = slug_counts.get(slug, 0) + 1

    # Track per-slug usage to append index if duplicates exist
    slug_used = {}
    generated = []

    for row in rows:
        base_slug = make_slug(row)
        if slug_counts[base_slug] > 1:
            n = slug_used.get(base_slug, 0) + 1
            slug_used[base_slug] = n
            slug = f"{base_slug}-{n}"
        else:
            slug = base_slug

        content = make_page(row)
        filepath = os.path.join(OUTPUT_DIR, f"{slug}.md")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        generated.append((slug, row["article_title"]))
        print(f"  wrote: articles/{slug}.md")

    print(f"\nGenerated {len(generated)} article pages in pubs/articles/")
    return generated


if __name__ == "__main__":
    main()
