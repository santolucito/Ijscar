#!/usr/bin/env python3
"""
Generate the Table of Contents page for an IJSCAR issue.

Edit the ARTICLES list below for each new issue, then run:
    python3 generate_toc_pdf.py
Output: toc.pdf

Matches the style of the TOC on page 3 of vol3-issue1.pdf.
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
from reportlab.lib import colors

# ── Configuration — update these for each new issue ───────────────────────────
VOLUME    = 3
ISSUE     = 2
DATE_LONG = "June 1, 2026"
OUTPUT    = "toc.pdf"

ARTICLES = [
    {
        "title":   "Visualizing Hyperparameters in 2D Drone Navigation",
        "authors": "Maanas Punuru, Jan Ole Ernst",
        "page":    4,
    },
    {
        "title":   "Entropy-Minimal Noise Schedules for Denoising Diffusion Probabilistic Models: "
                   "A Non-Equilibrium Thermodynamics Approach",
        "authors": "Tawhid Bin Omar",
        "page":    10,
    },
    {
        "title":   "Plexibot: A Homogeneous Modular Robot Framework for Adaptive Locomotion "
                   "in Unstructured Environments",
        "authors": "Kaavya Goel",
        "page":    16,
    },
    {
        "title":   "Usability of Municipal AI Policy Documents: A Heuristic Evaluation and "
                   "NLP Analysis Across 20 U.S. Cities",
        "authors": "Nikhil Mehra",
        "page":    23,
    },
    {
        "title":   "Backdoor Detection in Reinforcement Learning Agents for Electric Vehicle "
                   "Charging Control",
        "authors": "Ajay Raghavan",
        "page":    40,
    },
]
# ──────────────────────────────────────────────────────────────────────────────

GRAY  = colors.HexColor("#555555")
BLACK = colors.black
LIGHT = colors.HexColor("#eeeeee")

header_style = ParagraphStyle(
    "header", fontName="Times-Roman", fontSize=9,
    textColor=GRAY, alignment=TA_CENTER, spaceAfter=2,
)
title_style = ParagraphStyle(
    "title", fontName="Times-Bold", fontSize=14,
    textColor=BLACK, alignment=TA_CENTER, spaceBefore=18, spaceAfter=18,
)
article_title_style = ParagraphStyle(
    "atitle", fontName="Times-Bold", fontSize=10,
    textColor=BLACK, leading=13, spaceAfter=0,
)
author_style = ParagraphStyle(
    "author", fontName="Times-Italic", fontSize=9,
    textColor=GRAY, leading=13, spaceAfter=6,
)
page_style = ParagraphStyle(
    "pagenum", fontName="Times-Roman", fontSize=10,
    textColor=BLACK, alignment=TA_RIGHT,
)
footer_style = ParagraphStyle(
    "footer", fontName="Times-Roman", fontSize=8,
    textColor=GRAY, alignment=TA_CENTER, spaceBefore=4, spaceAfter=2,
)

doc = SimpleDocTemplate(
    OUTPUT, pagesize=letter,
    leftMargin=1.1*inch, rightMargin=1.1*inch,
    topMargin=0.9*inch, bottomMargin=1.0*inch,
)

story = []

# Header
story.append(Paragraph(f"Proceedings of IJSCAR, Volume {VOLUME}, Issue {ISSUE}", header_style))
story.append(Paragraph(DATE_LONG, header_style))
story.append(HRFlowable(width="100%", thickness=0.5, color=GRAY, spaceAfter=4))

# Title
story.append(Paragraph("Contents", title_style))

# Articles
usable_width = letter[0] - 2.2*inch   # full text width
page_col_w   = 0.45*inch
title_col_w  = usable_width - page_col_w

for art in ARTICLES:
    title_cell  = [Paragraph(art["title"],   article_title_style),
                   Paragraph(art["authors"], author_style)]
    page_cell   = Paragraph(str(art["page"]), page_style)

    t = Table(
        [[title_cell, page_cell]],
        colWidths=[title_col_w, page_col_w],
    )
    t.setStyle(TableStyle([
        ("VALIGN",    (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING",  (0,0), (-1,-1), 0),
        ("RIGHTPADDING", (0,0), (-1,-1), 0),
        ("TOPPADDING",   (0,0), (-1,-1), 0),
        ("BOTTOMPADDING",(0,0), (-1,-1), 6),
    ]))
    story.append(t)
    story.append(HRFlowable(width="100%", thickness=0.3, color=LIGHT, spaceAfter=4))

# Footer
story.append(Spacer(1, 0.3*inch))
story.append(HRFlowable(width="100%", thickness=0.5, color=GRAY, spaceAfter=4))
story.append(Paragraph(f"Volume {VOLUME}, Issue {ISSUE} &nbsp;&nbsp; {DATE_LONG}", footer_style))
story.append(Paragraph(
    f"© 2026 International Journal of Secondary Computing and Applications Research",
    footer_style
))

def _draw_page_number(canvas, doc):
    """Draw page number 3 at the bottom centre, matching acmart style."""
    canvas.saveState()
    canvas.setFont("Times-Roman", 9)
    canvas.setFillColor(GRAY)
    canvas.drawCentredString(letter[0] / 2, 0.5 * inch, "3")
    canvas.restoreState()

doc.build(story, onFirstPage=_draw_page_number, onLaterPages=_draw_page_number)
print(f"Wrote {OUTPUT}")
