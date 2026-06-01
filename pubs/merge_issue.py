#!/usr/bin/env python3
"""
Merge all components of an IJSCAR issue into a single PDF.

Usage:
    pip install pypdf        # one-time setup
    python3 merge_issue.py

Output: vol<VOLUME>-issue<ISSUE>.pdf in the pubs/ directory.
"""

from pypdf import PdfWriter

# ── Configuration — update these for each new issue ───────────────────────────
VOLUME = 3
ISSUE  = 2
OUTPUT = f"vol{VOLUME}-issue{ISSUE}.pdf"

# List PDFs in the order they should appear in the final issue.
# Paths are relative to this script (pubs/).
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
