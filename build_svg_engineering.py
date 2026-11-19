#!/usr/bin/env python3
"""Polaris engineering SVG generator — SOM-POL-0001 v0.4.0.
Hand-authored SVG per local-diagram-studio skill: LCARS roles, 4px grid,
gold on exactly 2 focals (GYST proofs rating bar, honest-zeros fence).
All copy measured from source artifacts 2026-11-18 (PROOFS.md, Atlas
BEATS, deployed-urls index, estate daily-state, crate/LOC count).
"""
import re

# --- semantic roles (never inline hex below) ---
PAPER = "#08090A"
PANEL = "#101214"
INK = "#E8E6E1"
MUTED = "#9A978E"
SOFT = "#565A60"
RULE = "#2A2D31"
ACCENT = "#C9A227"  # gold: LIVE / PROVEN / FOCAL only, 1-2 elements max

FONT = "ui-monospace, 'IBM Plex Mono', Menlo, Consolas, monospace"
W, H = 1200, 1560
MX = 48            # side margin
CW = W - 2 * MX    # 1104 content width

def esc(s: str) -> str:
    """Single-pass escape: & < > first, then unicode -> numeric entities."""
    s = s.replace("&", "&#38;").replace("<", "&#60;").replace(">", "&#62;")
    s = s.replace("\u00b7", "&#183;")   # middle dot
    s = s.replace("\u2014", "&#8212;")  # em dash
    s = s.replace("\u2013", "&#8211;")  # en dash
    s = s.replace("\u2019", "&#8217;")  # right single quote
    return s

parts = []
def add(s):
    parts.append(s)

def text(x, y, s, size=16, fill=INK, weight=None, ls=None, anchor=None):
    a = f' font-weight="{weight}"' if weight else ""
    b = f' letter-spacing="{ls}"' if ls else ""
    c = f' text-anchor="{anchor}"' if anchor else ""
    add(f'<text x="{x}" y="{y}" fill="{fill}" font-family="{FONT}" font-size="{size}"{a}{b}{c}>{esc(s)}</text>')

def rect(x, y, w, h, fill=None, stroke=None, sw=1):
    f = f' fill="{fill}"' if fill else ' fill="none"'
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}"{f}{st}/>')

# ================= canvas =================
add(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">')
rect(0, 0, W, H, fill=PAPER)

# ================= header =================
text(MX, 60, "SOMACOSF \u00b7 SOM-POL-0001-v0.4.0 \u00b7 ENGINEERING SCAN 2026-11-18", size=15, fill=MUTED, ls=3)
text(MX, 116, "THE ENGINEERING, RATED", size=44, fill=INK, weight="bold", ls=2)
text(MX, 152, "measured from source artifacts \u00b7 proofs record \u00b7 Atlas beat sheet \u00b7 deployed-URL index", size=17, fill=MUTED)
text(MX, 180, "ratings are evidence grades for the Polaris role, not quality scores", size=17, fill=MUTED)
rect(MX, 204, CW, 2, fill=RULE)

# ================= census strip =================
text(MX, 240, "CENSUS \u00b7 THE BUILD AS MEASURED", size=15, fill=MUTED, ls=3)
census = [
    ("20,211", "Atlas registry elements (6 types)"),
    ("16,701", "SCPM map splats"),
    ("447,453 MW", "EIA capacity graded PROVEN"),
    ("201,152", "proof mints \u00b7 0 collisions"),
    ("51 crates", "302,450 lines of Rust (Imbue)"),
    ("428", "deployed estate URLs \u00b7 85 records"),
]
cell_w = 352   # 3*352 + 2*24 = 1104
cell_h = 84
gap = 24
cy0 = 256
for i, (num, label) in enumerate(census):
    cx = MX + (i % 3) * (cell_w + gap)
    cyy = cy0 + (i // 3) * (cell_h + 16)
    rect(cx, cyy, cell_w, cell_h, fill=PANEL, stroke=RULE, sw=1)
    text(cx + 20, cyy + 40, num, size=28, fill=INK, weight="bold")
    text(cx + 20, cyy + 68, label, size=14, fill=MUTED)

census_end = cy0 + 2 * cell_h + 16  # 440
rect(MX, census_end + 16, CW, 2, fill=RULE)

# ================= segment ratings =================
seg_head_y = census_end + 52  # 492
text(MX, seg_head_y, "SEGMENT RATINGS \u00b7 SCALE 1\u20133 \u00b7 LABEL = WHAT IT EVIDENCES FOR POLARIS", size=15, fill=MUTED, ls=3)

segments = [
    # (name, scale, rating, gloss)
    ("GYST protocol core + proofs", "201,152 mints", 3, "claims re-run, not asserted: parity 1,200/1,200"),
    ("Atlas registry + i3 views", "20,211 elements", 3, "one registry; every view a function of it"),
    ("Agent coordination corpus", "5,556-line ledger", 3, "agents grading agents, with provenance"),
    ("Spoken ITPM + Revit evaluation", "15/15 integration", 3, "an eval in everything but name (SOM-DOC-10854)"),
    ("SCPM \u00b7 supply-chain map + feeds", "16,701 splats", 2, "capacity proven; snapshot, builder owed"),
    ("Estate + Says network", "11 city properties", 2, "428 surfaces; presentations over the registry"),
    ("Icoskin / icosphere", "126 files", 2, "claim boundary written before the claims"),
]
BAR_MAX = 360  # width for 3/3
row_y = seg_head_y + 28  # first row top = 520
ROW_H = 92
PITCH = 100
for i, (name, files, rating, gloss) in enumerate(segments):
    y = row_y + i * PITCH
    # name + files on one line
    text(MX, y + 24, name, size=20, fill=INK, weight="bold")
    name_w = len(name) * 12  # 20px mono ~12px/char
    text(MX + name_w + 24, y + 24, "\u00b7 " + files, size=17, fill=MUTED)
    # bar
    bw = BAR_MAX * rating // 3
    bar_fill = ACCENT if i == 0 else SOFT  # GOLD FOCAL 1: GYST proofs bar only
    rect(MX, y + 40, bw, 20, fill=bar_fill)
    rect(MX, y + 40, BAR_MAX, 20, fill=None, stroke=RULE, sw=1)
    text(MX + BAR_MAX + 20, y + 60, f"{rating} / 3", size=17, fill=MUTED)
    # gloss
    text(MX, y + 84, gloss, size=16, fill=MUTED)
    if i < len(segments) - 1:
        rect(MX, y + ROW_H + 4, CW, 1, fill=RULE)

seg_end = row_y + 6 * PITCH + ROW_H  # 520 + 600 + 92 = 1212

# ================= honest zeros fence (GOLD FOCAL 2) =================
fz_y = seg_end + 28  # 1240
fz_h = 132
rect(MX, fz_y, CW, fz_h, fill=PANEL, stroke=ACCENT, sw=2)
text(MX + 24, fz_y + 40, "HONEST ZEROS", size=17, fill=ACCENT, weight="bold", ls=3)
text(MX + 24, fz_y + 76, "0 production mints \u00b7 0 adopters \u00b7 $0 verified revenue", size=22, fill=INK, weight="bold")
text(MX + 24, fz_y + 108, "owed: anchor CANDIDATE_NOT_RATIFIED \u00b7 cross-shell SPEC \u00b7 SCPM builder missing", size=16, fill=MUTED)

# ================= footer =================
ft_y = fz_y + fz_h + 32  # 1404
rect(MX, ft_y, CW, 2, fill=RULE)
text(MX, ft_y + 40, "Ratings: Witness (Muse), 2026-11-18 \u00b7 scale 1\u20133 \u00b7 a 3 means the evidence would survive a Polaris grader;", size=15, fill=MUTED)
text(MX, ft_y + 68, "a 2 means it is real \u2014 and its cap is named on the row", size=15, fill=MUTED)

add("</svg>")
svg = "\n".join(parts) + "\n"

# grid audit: every x/y coordinate must be divisible by 4, as must
# structural widths/heights > 4 (hairline rects of 1-2px are exempt
# per the skill: "Hairlines 1-2px"; stroke widths likewise exempt)
coords = [int(n) for n in re.findall(r'(?:x|y)="(\d+)"', svg)]
bad = [n for n in coords if n % 4 != 0]
assert not bad, f"off-grid coordinates: {bad}"
sizes = [int(n) for n in re.findall(r'(?:width|height)="(\d+)"', svg)]
bad2 = [n for n in sizes if n > 4 and n % 4 != 0]
assert not bad2, f"off-grid structural sizes: {bad2}"
gold = svg.count(ACCENT)
print(f"gold occurrences in markup: {gold} (bar rect + fence stroke + fence heading = 3 refs, 2 elements)")

import os
os.makedirs("/home/hatch/workspace/polaris/assets", exist_ok=True)
os.makedirs("/home/hatch/workspace/polaris/site/assets", exist_ok=True)
with open("/home/hatch/workspace/polaris/assets/polaris-engineering.svg", "w") as f:
    f.write(svg)
with open("/home/hatch/workspace/polaris/site/assets/polaris-engineering.svg", "w") as f:
    f.write(svg)
print("wrote polaris-engineering.svg", len(svg), "bytes")
