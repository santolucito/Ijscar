#!/usr/bin/env python3
"""
Generate the Editor-in-Chief letter page as a PDF.

Reads content from editor-letter.md and produces editor-letter.pdf,
styled to match the existing IJSCAR issue format.

Usage:
    pip install reportlab
    python3 generate_letter_pdf.py

Output: editor-letter.pdf  (drop into COMPONENTS list in merge_issue.py)
"""

import re
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable
)
from reportlab.lib import colors

# ── Read editor-letter.md ──────────────────────────────────────────────────────

def parse_letter_md(path="editor-letter.md"):
    with open(path, encoding="utf-8") as f:
        raw = f.read()

    # Pull front-matter fields
    fm_match = re.search(r"^---\n(.*?)\n---", raw, re.DOTALL)
    meta = {}
    if fm_match:
        for line in fm_match.group(1).splitlines():
            if ":" in line and not line.startswith("#"):
                key, _, val = line.partition(":")
                meta[key.strip()] = val.strip().strip('"')

    # Body = everything after the closing ---
    body_start = raw.find("---", raw.find("---") + 3) + 3
    body = raw[body_start:].strip()

    # Split into title + paragraphs
    lines = body.splitlines()
    title = ""
    paragraphs = []
    current = []

    for line in lines:
        if line.startswith("# "):
            title = line[2:].strip()
        elif line.strip() == "":
            if current:
                paragraphs.append(" ".join(current).strip())
                current = []
        else:
            current.append(line.strip())
    if current:
        paragraphs.append(" ".join(current).strip())

    return meta, title, paragraphs


meta, title, paragraphs = parse_letter_md()

volume    = meta.get("volume", "X")
issue     = meta.get("issue", "X")
month     = meta.get("month", "")
year      = meta.get("year", "")
date_long = meta.get("date_long", f"{month} {year}")
doi       = meta.get("issue_doi", "")
url       = meta.get("issue_url", "")

# ── Styles ─────────────────────────────────────────────────────────────────────

GRAY  = colors.HexColor("#555555")
BLACK = colors.black

header_style = ParagraphStyle(
    "header",
    fontName="Times-Roman",
    fontSize=9,
    textColor=GRAY,
    alignment=TA_CENTER,
    spaceAfter=2,
)

title_style = ParagraphStyle(
    "title",
    fontName="Times-Bold",
    fontSize=14,
    textColor=BLACK,
    alignment=TA_CENTER,
    spaceBefore=18,
    spaceAfter=18,
)

body_style = ParagraphStyle(
    "body",
    fontName="Times-Roman",
    fontSize=10,
    leading=13.5,
    alignment=TA_JUSTIFY,
    spaceAfter=7,
)

sig_style = ParagraphStyle(
    "sig",
    fontName="Times-Roman",
    fontSize=10,
    leading=13.5,
    alignment=TA_LEFT,
    spaceBefore=4,
    spaceAfter=3,
)

footer_style = ParagraphStyle(
    "footer",
    fontName="Times-Roman",
    fontSize=8,
    textColor=GRAY,
    alignment=TA_CENTER,
    spaceBefore=4,
    spaceAfter=2,
)

# ── Build PDF ──────────────────────────────────────────────────────────────────

OUTPUT = "editor-letter.pdf"

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=letter,
    leftMargin=1.1 * inch,
    rightMargin=1.1 * inch,
    topMargin=0.75 * inch,
    bottomMargin=0.75 * inch,
)

story = []

# Page header
story.append(Paragraph(
    f"Proceedings of International Journal of Secondary Computing and Applications Research, "
    f"Vol {volume}, Issue {issue}",
    header_style
))
story.append(Paragraph(date_long, header_style))
story.append(HRFlowable(width="100%", thickness=0.5, color=GRAY, spaceAfter=4))

# Letter title
story.append(Paragraph(title, title_style))

# Split at "Sincerely" — everything before is body, from there on is sign-off
signoff_idx = next(
    (i for i, p in enumerate(paragraphs) if p.startswith("Sincerely")),
    len(paragraphs)
)
body_paras   = paragraphs[:signoff_idx]
signoff_paras = paragraphs[signoff_idx:]

for para in body_paras:
    story.append(Paragraph(para, body_style))

# Signature block
story.append(Spacer(1, 0.15 * inch))
for para in signoff_paras:
    for line in para.splitlines():
        story.append(Paragraph(line.strip(), sig_style))

# Footer
story.append(Spacer(1, 0.3 * inch))
story.append(HRFlowable(width="100%", thickness=0.5, color=GRAY, spaceAfter=4))
story.append(Paragraph(
    f"Volume {volume}, Issue {issue} &nbsp;&nbsp; {date_long}",
    footer_style
))
if doi:
    story.append(Paragraph(
        f"DOI: {doi} | {url}",
        footer_style
    ))
story.append(Paragraph(
    f"© {year} International Journal of Secondary Computing and Applications Research",
    footer_style
))

def _draw_page_number(canvas, doc):
    """Draw page number 2 at the bottom centre, matching acmart style."""
    canvas.saveState()
    canvas.setFont("Times-Roman", 9)
    canvas.setFillColor(GRAY)
    canvas.drawCentredString(letter[0] / 2, 0.5 * inch, "2")
    canvas.restoreState()

doc.build(story, onFirstPage=_draw_page_number, onLaterPages=_draw_page_number)
print(f"Wrote {OUTPUT}")
