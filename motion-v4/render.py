#!/usr/bin/env python3
"""POLARIS v0.4.0 — the engineering, rated. Deterministic program-motion (PIL -> frames).
240 frames @ 12fps = 20.0s, 1280x720. Beats per BEATS.md v0.4.0.
Facts: PROOFS.md (SOM-DOC-10542), Atlas BEATS (SOM-DOC-10741), deployed-urls
index, estate daily-state — all read 2026-11-18. No private workstream appears.
Brand: paper #08090A, ink #E8E6E1, muted #9A978E, gold #C9A227 focal only.
All text inside y in [60, 660].
"""
from PIL import Image, ImageDraw, ImageFont

W, H, FPS = 1280, 720, 12
PER = 4 * FPS               # 48 frames per beat
TOTAL = 5 * PER             # 240
BG = (8, 9, 10)
PANEL_LINE = (43, 45, 48)
INK = (232, 230, 225)
MUT = (154, 151, 142)
GOLD = (201, 162, 39)

FD = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"

def f(sz, b=False):
    return ImageFont.truetype(FB if b else FD, sz)

F_EYE = f(15, True)
F_KICK = f(15, True)
F_TITLE = f(36, True)
F_SUB = f(23)
F_SUBB = f(23, True)
F_NUM = f(32, True)
F_LAB = f(21)
F_RLAB = f(23, True)
F_SCORE = f(23, True)
F_NAME = f(23, True)
F_NOTE = f(18)
F_BIG0 = f(72, True)
F_BIGLAB = f(20)
F_OWED = f(22, True)
F_CLOSE = f(28, True)
F_CAP = f(17, True)
F_FOOT = f(14)

MX = 72  # left margin

def chrome(d, beat_idx, kicker, foot, frame_no):
    d.rectangle([40, 40, W - 40, H - 40], outline=PANEL_LINE, width=2)
    d.text((MX, 66), "POLARIS - RESEARCH ENGINEER - GOOGLE DEEPMIND", font=F_EYE, fill=MUT)
    r = "SOMACOSF"
    d.text((W - MX - d.textlength(r, font=F_EYE), 66), r, font=F_EYE, fill=MUT)
    d.line([(MX, 100), (W - MX, 100)], fill=PANEL_LINE, width=2)
    d.text((MX, 118), kicker, font=F_KICK, fill=MUT)
    d.text((MX, 632), foot, font=F_FOOT, fill=MUT)
    fr = f"frame {frame_no}/{TOTAL}"
    d.text((W - MX - d.textlength(fr, font=F_FOOT), 632), fr, font=F_FOOT, fill=MUT)

def caption(d, text):
    d.text((MX, 594), text, font=F_CAP, fill=INK)

def gate(u, t):
    return u >= t

# ---------------------------------------------------------------- beat 1
def beat1(d, u):
    # title: "The corpus, " ink + "rated." gold (focal)
    t1 = "The engineering, "
    d.text((MX, 148), t1, font=F_TITLE, fill=INK)
    x2 = MX + d.textlength(t1, font=F_TITLE)
    d.text((x2, 148), "rated.", font=F_TITLE, fill=GOLD)
    tw = x2 + d.textlength("rated.", font=F_TITLE) - MX
    if gate(u, 0.25):
        d.line([(MX, 204), (MX + tw, 204)], fill=GOLD, width=3)
    if gate(u, 0.35):
        d.text((MX, 248), "The applicant's corpus build - substrate, atlas, estate -", font=F_SUB, fill=INK)
    if gate(u, 0.5):
        d.text((MX, 286), "measured ", font=F_SUBB, fill=INK)
        x = MX + d.textlength("measured ", font=F_SUBB)
        d.text((x, 286), "- not described.", font=F_SUB, fill=MUT)
    if gate(u, 0.7):
        d.text((MX, 356), "UUID substrate. i3 views. SCPM. 428 deployed surfaces,", font=F_NOTE, fill=MUT)
        d.text((MX, 382), "counted below before it is characterised.", font=F_NOTE, fill=MUT)
    caption(d, "THE DOSSIER, AS A FILM: COUNTED FIRST, RATED SECOND.")

# ---------------------------------------------------------------- beat 2
CENSUS = [
    ("20,211", "Atlas registry elements"),
    ("16,701", "SCPM map splats"),
    ("447,453", "MW - EIA capacity PROVEN"),
    ("201,152", "proof mints - 0 collisions"),
    ("51", "crates - 302,450 lines of Rust"),
]

def beat2(d, u):
    d.text((MX, 148), "The census", font=F_TITLE, fill=INK)
    y = 224
    for i, (num, lab) in enumerate(CENSUS):
        if gate(u, 0.08 + i * 0.13):
            nw = d.textlength(num, font=F_NUM)
            d.text((372 - nw, y), num, font=F_NUM, fill=INK)
            d.text((404, y + 7), lab, font=F_LAB, fill=MUT)
            if i < len(CENSUS) - 1:
                d.line([(MX, y + 52), (W - MX, y + 52)], fill=PANEL_LINE, width=1)
        y += 64
    caption(d, "MEASURED FROM SOURCE ARTIFACTS, 2026-11-18.")

# ---------------------------------------------------------------- beat 3
RATINGS = [
    ("Designing eval tasks", 2),
    ("Evaluating model weaknesses", 3),
    ("Building data and pipelines", 2),
]

def beat3(d, u):
    d.text((MX, 148), "Rated against the posting", font=F_TITLE, fill=INK)
    y = 232
    for i, (lab, score) in enumerate(RATINGS):
        if gate(u, 0.1 + i * 0.18):
            d.text((MX, y), lab, font=F_RLAB, fill=INK)
            bx = 800
            for k in range(3):
                x0 = bx + k * 52
                if k < score:
                    fill = GOLD if score == 3 else INK
                    d.rectangle([x0, y, x0 + 38, y + 34], fill=fill)
                else:
                    d.rectangle([x0, y, x0 + 38, y + 34], outline=PANEL_LINE, width=2)
            d.text((bx + 3 * 52 + 18, y + 3), f"{score} / 3", font=F_SCORE,
                   fill=GOLD if score == 3 else MUT)
        y += 104
    caption(d, "WITNESS SCALE 1-3 - THE POSTING'S THREE RESPONSIBILITIES.")

# ---------------------------------------------------------------- beat 4
def beat4(d, u):
    d.text((MX, 148), "Segments, rated", font=F_TITLE, fill=INK)
    rows = [
        ("GYST proofs", 3, ["claims re-run - parity 1,200/1,200"]),
        ("Atlas + i3", 3, ["every view a function of the registry"]),
        ("SCPM", 2, ["snapshot - regeneration builder owed"]),
        ("Estate + Says", 2, ["presentations over the registry"]),
    ]
    y = 216
    for i, (name, score, notes) in enumerate(rows):
        if gate(u, 0.08 + i * 0.16):
            d.text((MX, y), name, font=F_NAME, fill=GOLD if score == 3 else INK)
            d.text((300, y), f"{score} / 3", font=F_SCORE, fill=MUT)
            ny = y + 36
            for ln in notes:
                d.text((300, ny), ln, font=F_NOTE, fill=MUT)
                ny += 26
        y += 62 + 26 * len(notes) + (10 if notes else 0)
    caption(d, "SAME SCALE - THE ENGINEERING SEGMENTS OF SECTION 07.")

# ---------------------------------------------------------------- beat 5
def beat5(d, u):
    d.text((MX, 148), "The honest close", font=F_TITLE, fill=INK)
    if gate(u, 0.15):
        d.text((MX, 232), "0", font=F_BIG0, fill=INK)
        d.text((MX, 322), "production mints", font=F_BIGLAB, fill=MUT)
        d.text((360, 232), "0", font=F_BIG0, fill=INK)
        d.text((360, 322), "adopters", font=F_BIGLAB, fill=MUT)
    if gate(u, 0.45):
        y = 392
        d.text((MX, y), "solo Polaris-shaped task - ", font=F_OWED, fill=INK)
        x = MX + d.textlength("solo Polaris-shaped task - ", font=F_OWED)
        d.text((x, y), "OWED", font=F_OWED, fill=GOLD)
    if gate(u, 0.58):
        d.text((MX, 428), "GeoHex anchor CANDIDATE_NOT_RATIFIED - SCPM builder missing", font=F_NOTE, fill=MUT)
    if gate(u, 0.72):
        d.text((MX, 468), "rated, not inflated.", font=F_CLOSE, fill=GOLD)
    caption(d, "THE ZEROS STAY ON THE CARD.")

BEATS = [
    ("01 / 05 - HERO", "POLARIS DOSSIER v0.4.0 - THE ENGINEERING, RATED", beat1),
    ("02 / 05 - CENSUS", "COUNTS MEASURED FROM SOURCE ARTIFACTS, 2026-11-18", beat2),
    ("03 / 05 - RATINGS", "WITNESS SCALE 1-3 - NO CLAIM UPGRADED", beat3),
    ("04 / 05 - SEGMENTS", "SEGMENT RATINGS - WITNESS SCALE 1-3", beat4),
    ("05 / 05 - HONEST CLOSE", "SOM-POL-0001 - SOM-DOC-10858 - POLARIS.SOMACOSF.COM", beat5),
]

import os
os.makedirs("frames", exist_ok=True)
for i in range(TOTAL):
    b = i // PER
    u = (i % PER) / PER
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    kicker, foot, fn = BEATS[b]
    chrome(d, b, kicker, foot, i + 1)
    fn(d, u)
    img.save(f"frames/f{i:04d}.png")
print("frames", TOTAL)
