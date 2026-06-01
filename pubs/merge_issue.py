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
    # ← DROP your cover page PDF here (export from Canva as PDF, put in pubs/)
    "cover-vol3-issue2.pdf",
    "editor-letter.pdf",
    "toc.pdf",
    "/Users/mariahwang/Downloads/1_Hyperparameters_in_Drone_Navigation_Maanas_FINAL/main.pdf",
    "/Users/mariahwang/Downloads/2_Entropy_Minimal_Noise_Schedules_for_DDPMs_Tawhid_FINAL/main.pdf",
    "/Users/mariahwang/Downloads/3_A_Homogeneous_Modular_Robot_for_Adaptive_Locomotion_GOEL_FINAL/ARTICLE.pdf",
    "/Users/mariahwang/Downloads/4_Municipal_AI_Policy_Usability_NIKHIL_FINAL/Municipal_AI_Policy_IJSCAR_Overleaf/main.pdf",
    "/Users/mariahwang/Downloads/5_Backdoor_Detection_in_RL_EV_Charging_AJAY_FINAL/main.pdf",
]
# ──────────────────────────────────────────────────────────────────────────────

writer = PdfWriter()

for path in COMPONENTS:
    writer.append(path)
    print(f"  added: {path}")

with open(OUTPUT, "wb") as f:
    writer.write(f)

print(f"\nDone — wrote {OUTPUT}")
