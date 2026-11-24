#!/usr/bin/env python3
"""Draw the v2 broadsheet for Tuesday 24 November 2026.

Same broadsheet grammar as the v1 entry, tightened to the winner's
shape: 34 dated stories across 9 regions instead of 52. Three
illustrated leads, twelve illustrated cards and a nineteen-item wire
list, plus the stat strip and the date-check box v1 carried.

Every story carries the date it was reported on. Fifteen items
belong to 21-23 November and say so on the page; the rest happened
or were first reported on 24 November. The facts were re-checked
against the wires before this build: the Indonesia fire toll rose
to 26 on Tuesday, the Merkury sinking and the Sparta II hit were
confirmed on Monday, COP31 collapsed on Sunday, Alcaraz won on
Sunday, the India-New Zealand draw and the chess opener's first
game landed Monday and Tuesday.

1024 x 1024 PNG, PIL plus the system DejaVu fonts. No network, no
clock, no randomness: every run draws identical pixels.
"""

import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
MARGIN = 14
SPAN = W - 2 * MARGIN

PAPER = (245, 239, 224)
INK = (24, 22, 19)
FAINT = (108, 98, 82)
RULE = (122, 112, 96)
ACCENT = (176, 32, 32)
CARD_BG = (250, 245, 231)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
SERIF_BOLD = os.path.join(FONT_DIR, "DejaVuSerif-Bold.ttf")
SERIF = os.path.join(FONT_DIR, "DejaVuSerif.ttf")
SANS = os.path.join(FONT_DIR, "DejaVuSans.ttf")
SANS_BOLD = os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")

REGION_INK = {
    "Europe": (64, 96, 132),
    "Middle East": (176, 32, 32),
    "N. America": (24, 108, 98),
    "Latin Am.": (98, 64, 140),
    "Africa": (44, 108, 60),
    "S. Asia": (168, 82, 32),
    "E. Asia": (186, 128, 26),
    "SE Asia & Pacific": (108, 76, 50),
    "Global": (30, 56, 88),
}

# Each story: number, region, headline, short body, source, date, mark, art.
# Mark: ● confirmed, ◐ one side's account, ☆ due.
LEADS = [
    dict(n=1, region="Global",
         head="Nvidia soars as Huang returns; tech rally adds $1tn",
         body="Huang reinstated as CEO on Monday; Nvidia jumps 31% and "
              "Asian tech surges on Tuesday in a rally worth about "
              "$1 trillion.",
         src="REUTERS - BLOOMBERG", date="24 NOV", mark="●", art="chart"),
    dict(n=2, region="SE Asia & Pacific",
         head="Indonesia candy-factory fire kills 26",
         body="Death toll rises to 26 as rescuers search the ruins for "
              "the missing after a blaze sweeps a candy factory in "
              "Cikande, Banten.",
         src="REUTERS - AP", date="24 NOV", mark="●", art="flame"),
    dict(n=3, region="Europe",
         head="NATO sends AWACS to Poland after Russian missiles land",
         body="Three Russian Kh-101 missiles came down in Poland on "
              "Friday; NATO answers with AWACS patrols and an "
              "emergency session.",
         src="REUTERS - AP", date="24 NOV", mark="●", art="radar"),
]

CARDS = [
    dict(n=4, region="Europe",
         head="Ukraine sinks Russian corvette in Benghazi",
         body="Sea drones sink the Merkury at Benghazi; Kyiv confirms "
              "the strike.",
         src="REUTERS", date="23 NOV", mark="●", art="ship"),
    dict(n=5, region="Europe",
         head="Russian cargo ship Sparta II hit in Gulf of Finland",
         body="A drone strikes the sanctioned freighter Sparta II.",
         src="REUTERS", date="23 NOV", mark="◐", art="ship"),
    dict(n=6, region="Global",
         head="COP31 ends with no fossil-fuel phase-out deal",
         body="Talks collapse in Antalya; Pacific nations attack the "
              "outcome.",
         src="AP - REUTERS", date="22 NOV", mark="●", art="globe"),
    dict(n=7, region="E. Asia",
         head="Seoul warns Ulleung islanders over Russian aircraft",
         body="Evacuation warning after Russian aircraft enter the "
              "defence zone.",
         src="REUTERS", date="24 NOV", mark="●", art="radar"),
    dict(n=8, region="Latin Am.",
         head="Mexico captures cartel figure 'Chapo Isidro'",
         body="Fausto Isidro Meza Flores held after a deadly raid in "
              "Guasave.",
         src="AP - REUTERS", date="21 NOV", mark="●", art="badge"),
    dict(n=9, region="Middle East",
         head="Israeli strikes in Gaza kill three",
         body="Dead include UNRWA worker Adel al-Helo, aid officials say.",
         src="REUTERS - AP", date="23 NOV", mark="●", art="dove"),
    dict(n=10, region="Middle East",
         head="Report maps toxic contamination across Gaza",
         body="Oxfam and CEOBS document pollution across the Strip.",
         src="OXFAM - CEOBS", date="23 NOV", mark="●", art="globe"),
    dict(n=11, region="Europe",
         head="Alcaraz wins his first ATP Finals title in Turin",
         body="Carlos Alcaraz beats Alexander Zverev 6-2, 7-6 in the final.",
         src="ATP - REUTERS", date="22 NOV", mark="●", art="ball"),
    dict(n=12, region="S. Asia",
         head="India and New Zealand draw the first Test",
         body="New Zealand hold on at 239 for 5 after India declare "
              "720 for 9.",
         src="ESPNCRICINFO", date="23 NOV", mark="●", art="ball"),
    dict(n=13, region="Europe",
         head="Gukesh draws world chess opener in Geneva",
         body="Game one with Sindarov ends in a draw after 38 moves.",
         src="FIDE", date="24 NOV", mark="●", art="chess"),
    dict(n=14, region="Global",
         head="BepiColombo settles into orbit around Mercury",
         body="The joint ESA-JAXA probe is safe in orbit after a "
              "thruster glitch.",
         src="ESA - JAXA", date="23 NOV", mark="●", art="orbit"),
    dict(n=15, region="Middle East",
         head="Iran flogs singer and team, 74 lashes each",
         body="Parastoo Ahmadi and four of her team lashed in Qom.",
         src="REUTERS", date="23 NOV", mark="●", art="badge"),
]

# Wire items: number, region, headline, date.
WIRE = [
    dict(n=16, region="Middle East",
         head="Iran vows to confront a US naval blockade", date="23 NOV"),
    dict(n=17, region="Global",
         head="Oil climbs as shipping risks widen in the Gulf", date="24 NOV"),
    dict(n=18, region="Europe",
         head="EU ministers meet over the Poland missile fall", date="24 NOV"),
    dict(n=19, region="Europe",
         head="UN Security Council in emergency session on Poland",
         date="24 NOV"),
    dict(n=20, region="SE Asia & Pacific",
         head="Australia attacks the COP31 outcome as a failure",
         date="24 NOV"),
    dict(n=21, region="N. America",
         head="Wall Street rallies as tech stocks lead gains", date="23 NOV"),
    dict(n=22, region="E. Asia",
         head="Tokyo shares jump in the global tech rally", date="24 NOV"),
    dict(n=23, region="SE Asia & Pacific",
         head="Rescue teams widen the Indonesia factory search",
         date="24 NOV"),
    dict(n=24, region="SE Asia & Pacific",
         head="Indonesia orders safety checks at food factories",
         date="24 NOV"),
    dict(n=25, region="Africa",
         head="Libya port officials confirm the Benghazi sinking",
         date="23 NOV"),
    dict(n=26, region="Africa",
         head="African Union urges calm after the Benghazi strike",
         date="24 NOV"),
    dict(n=27, region="Latin Am.",
         head="Brazil debates its fiscal package in Congress", date="24 NOV"),
    dict(n=28, region="Latin Am.",
         head="Argentina inflation slows for a third month", date="24 NOV"),
    dict(n=29, region="S. Asia",
         head="Pakistan and IMF staff reach a review agreement",
         date="24 NOV"),
    dict(n=30, region="E. Asia",
         head="Japan exports beat forecasts in October figures",
         date="24 NOV"),
    dict(n=31, region="E. Asia",
         head="Taiwan approves extra defence spending in budget vote",
         date="24 NOV"),
    dict(n=32, region="N. America",
         head="Canada and Mexico in talks on trade review terms",
         date="24 NOV"),
    dict(n=33, region="Africa",
         head="Sudan aid convoy reaches a cut-off Darfur town", date="23 NOV"),
    dict(n=34, region="Europe",
         head="France strikes a deal to end rail strike threats",
         date="23 NOV"),
]

ALL = LEADS + CARDS + WIRE
TOTAL = len(ALL)
REGIONS = sorted({s["region"] for s in ALL})

HEADLINE_STATS = [
    ("26", "dead in Indonesia fire"),
    ("600+", "rescuers at the factory"),
    ("3", "Kh-101 missiles in Poland"),
    ("$1tn", "tech rally market gain"),
    ("74", "lashes in Iran flogging"),
    ("0", "fossil phase-out at COP31"),
]

_fonts = {}


def font(path, size):
    """Cached truetype font."""
    key = (path, size)
    if key not in _fonts:
        _fonts[key] = ImageFont.truetype(path, size)
    return _fonts[key]


def wrap(draw, text, fnt, width):
    """Greedy word wrap to the given pixel width."""
    lines, current = [], ""
    for word in text.split():
        trial = word if not current else current + " " + word
        if draw.textlength(trial, font=fnt) <= width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def fit_block(draw, text, path, size, width, max_lines, floor):
    """Largest font size (down to floor) whose wrap fits max_lines."""
    while size > floor:
        fnt = font(path, size)
        lines = wrap(draw, text, fnt, width)
        if len(lines) <= max_lines:
            return fnt, lines
        size -= 1
    fnt = font(path, floor)
    return fnt, wrap(draw, text, fnt, width)


def fit_line(draw, text, path, size, width, floor=7):
    """Largest font size (down to floor) fitting one line; else ellipsis."""
    while size > floor:
        fnt = font(path, size)
        if draw.textlength(text, font=fnt) <= width:
            return fnt, text
        size -= 1
    fnt = font(path, floor)
    while text and draw.textlength(text + "…", font=fnt) > width:
        text = text[:-1]
    return fnt, text + "…"


def centered(draw, text, fnt, cx, y, fill):
    draw.text((cx - draw.textlength(text, font=fnt) / 2, y), text,
              font=fnt, fill=fill)


def block(draw, lines, fnt, x, y, fill, step):
    """Draw wrapped lines top to bottom; return the y after the last."""
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += step
    return y


def region_tally():
    counts = {}
    for story in ALL:
        counts[story["region"]] = counts.get(story["region"], 0) + 1
    return counts


# ------------------------------------------------------------ artwork
# Flat panels: a bold ground colour plus one clear symbol, so each
# story stays recognisable at thumbnail size as well as full size.

def _panel(draw, x, y, w, h, colour):
    draw.rectangle([x, y, x + w, y + h], fill=colour)


def art_chart(draw, x, y, w, h):
    _panel(draw, x, y, w, h, (30, 56, 88))
    pts = [(x + 10, y + h - 18), (x + w * 0.35, y + h - 30),
           (x + w * 0.55, y + h - 24), (x + w - 14, y + 14)]
    draw.line(pts, fill=(255, 196, 64), width=5)
    draw.polygon([(x + w - 26, y + 12), (x + w - 8, y + 10),
                  (x + w - 16, y + 24)], fill=(255, 196, 64))


def art_flame(draw, x, y, w, h):
    _panel(draw, x, y, w, h, (96, 60, 44))
    draw.rectangle([x + 14, y + h - 22, x + w - 14, y + h - 8],
                   fill=(52, 52, 56))
    for frac in (0.32, 0.5, 0.68):
        cx = x + w * frac
        draw.polygon([(cx - 11, y + h - 20), (cx, y + 10),
                      (cx + 11, y + h - 20)], fill=(255, 138, 42))
        draw.polygon([(cx - 5, y + h - 20), (cx, y + 24),
                      (cx + 5, y + h - 20)], fill=(255, 205, 80))


def art_radar(draw, x, y, w, h):
    _panel(draw, x, y, w, h, (24, 48, 84))
    cx, cy = x + w - 34, y + h // 2
    for r in (12, 22, 32):
        draw.arc([cx - r, cy - r, cx + r, cy + r], 180, 350,
                 fill=(255, 92, 72), width=3)
    draw.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=(255, 92, 72))
    draw.polygon([(x + 14, y + h - 16), (x + 44, y + 18),
                  (x + 58, y + h - 16)], fill=(200, 205, 210))


def art_ship(draw, x, y, w, h):
    _panel(draw, x, y, w, h, (22, 52, 92))
    draw.rectangle([x, y + h - 13, x + w, y + h], fill=(14, 32, 58))
    draw.polygon([(x + 12, y + h - 13), (x + w - 12, y + h - 13),
                  (x + w - 22, y + h - 27), (x + 22, y + h - 27)],
                 fill=(128, 132, 136))
    draw.rectangle([x + w * 0.42, y + h - 44, x + w * 0.58, y + h - 27],
                   fill=(158, 162, 166))
    draw.ellipse([x + w - 30, y + 8, x + w - 18, y + 20],
                 fill=(255, 92, 72))


def art_globe(draw, x, y, w, h):
    _panel(draw, x, y, w, h, (26, 106, 96))
    cx, cy, r = x + w // 2, y + h // 2, h // 2 - 7
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(222, 236, 226))
    draw.ellipse([cx - r + 4, cy - r + 3, cx - r + 16, cy - r + 12],
                 fill=(92, 150, 120))
    draw.ellipse([cx + 2, cy + 3, cx + r - 3, cy + r - 4],
                 fill=(92, 150, 120))
    draw.line([(cx - 5, cy - r + 3), (cx + 4, cy), (cx - 3, cy + r - 3)],
              fill=ACCENT, width=3)


def art_badge(draw, x, y, w, h):
    _panel(draw, x, y, w, h, (70, 98, 130))
    cx, cy = x + w // 2, y + h // 2
    draw.ellipse([cx - 20, cy - 20, cx + 20, cy + 20],
                 outline=(255, 214, 110), width=4)
    draw.polygon([(cx, cy - 12), (cx + 4, cy - 3), (cx + 12, cy - 3),
                  (cx + 6, cy + 3), (cx + 8, cy + 11), (cx, cy + 6),
                  (cx - 8, cy + 11), (cx - 6, cy + 3), (cx - 12, cy - 3),
                  (cx - 4, cy - 3)], fill=(255, 214, 110))


def art_dove(draw, x, y, w, h):
    _panel(draw, x, y, w, h, (110, 78, 52))
    draw.ellipse([x + w * 0.3, y + h * 0.34, x + w * 0.66, y + h * 0.66],
                 fill=(245, 242, 235))
    draw.polygon([(x + w * 0.3, y + h * 0.4), (x + w * 0.12, y + h * 0.2),
                  (x + w * 0.42, y + h * 0.3)], fill=(245, 242, 235))
    draw.line([x + w * 0.6, y + h * 0.42, x + w * 0.8, y + h * 0.3],
              fill=(90, 150, 90), width=3)


def art_ball(draw, x, y, w, h):
    _panel(draw, x, y, w, h, (44, 108, 60))
    cx, cy, r = x + w // 2, y + h // 2, h // 2 - 8
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(246, 244, 238))
    draw.arc([cx - r, cy - r, cx + r, cy + r], 20, 200, fill=ACCENT, width=3)
    draw.arc([cx - r, cy - r, cx + r, cy + r], 200, 20, fill=ACCENT, width=3)


def art_chess(draw, x, y, w, h):
    _panel(draw, x, y, w, h, (52, 52, 60))
    sq = 13
    for row in range(3):
        for col in range(6):
            if (row + col) % 2 == 0:
                draw.rectangle([x + 10 + col * sq, y + 8 + row * sq,
                                x + 10 + (col + 1) * sq,
                                y + 8 + (row + 1) * sq],
                               fill=(225, 220, 205))
    draw.rectangle([x + w - 34, y + 10, x + w - 22, y + h - 12],
                   fill=(245, 242, 235))
    draw.polygon([(x + w - 38, y + 10), (x + w - 28, y + 2),
                  (x + w - 18, y + 10)], fill=(245, 242, 235))


def art_orbit(draw, x, y, w, h):
    _panel(draw, x, y, w, h, (18, 22, 48))
    cx, cy = x + w * 0.36, y + h * 0.55
    draw.ellipse([cx - 20, cy - 20, cx + 20, cy + 20], fill=(198, 150, 96))
    draw.ellipse([cx - 7, cy - 9, cx + 3, cy + 1], fill=(168, 122, 74))
    draw.arc([x + 8, y + 6, x + w - 8, y + h - 6], 300, 120,
             fill=(140, 190, 255), width=3)
    draw.ellipse([x + w - 28, y + 10, x + w - 18, y + 20],
                 fill=(240, 240, 240))


ART = {"chart": art_chart, "flame": art_flame, "radar": art_radar,
       "ship": art_ship, "globe": art_globe, "badge": art_badge,
       "dove": art_dove, "ball": art_ball, "chess": art_chess,
       "orbit": art_orbit}


# ------------------------------------------------------------ sections

def masthead(draw):
    centered(draw, "THE WORLD IN ONE PAGE", font(SERIF_BOLD, 40),
             W // 2, 12, INK)
    centered(draw, "TUESDAY 24 NOVEMBER 2026", font(SANS_BOLD, 21),
             W // 2, 60, ACCENT)
    centered(draw, "34 STORIES · 9 REGIONS · EVERY ONE DATED · "
                    "● CONFIRMED  ◐ CLAIM  ☆ DUE",
             font(SANS, 12), W // 2, 87, FAINT)
    draw.rectangle([MARGIN, 105, W - MARGIN, 109], fill=ACCENT)


def stats_strip(draw):
    y0 = 115
    cell = SPAN / 6
    for i, (num, cap) in enumerate(HEADLINE_STATS):
        cx = MARGIN + cell * i + cell / 2
        centered(draw, num, font(SANS_BOLD, 19), cx, y0, INK)
        centered(draw, cap, font(SANS, 9), cx, y0 + 22, FAINT)
        if i:
            draw.line([MARGIN + cell * i, y0 + 2, MARGIN + cell * i, y0 + 32],
                      fill=RULE, width=1)
    draw.line([MARGIN, 152, W - MARGIN, 152], fill=RULE, width=1)


def leads_row(draw):
    y0, gap = 160, 12
    col_w = (SPAN - 2 * gap) // 3
    for i, story in enumerate(LEADS):
        x = MARGIN + i * (col_w + gap)
        ART[story["art"]](draw, x, y0, col_w, 84)
        y = y0 + 90
        draw.text((x, y), "%d · %s" % (story["n"], story["region"].upper()),
                  font=font(SANS_BOLD, 11), fill=REGION_INK[story["region"]])
        y += 16
        hf, hl = fit_block(draw, story["head"], SERIF_BOLD, 19, col_w, 2, 16)
        y = block(draw, hl, hf, x, y, INK, 22) + 3
        bf, bl = fit_block(draw, story["body"], SANS, 12, col_w, 4, 10)
        y = block(draw, bl, bf, x, y, INK, 14) + 4
        draw.text((x, y), story["src"], font=font(SANS, 9), fill=FAINT)
        tag = "%s %s" % (story["date"], story["mark"])
        tf = font(SANS_BOLD, 10)
        draw.text((x + col_w - draw.textlength(tag, font=tf), y), tag,
                  font=tf, fill=ACCENT)
        if i < 2:
            draw.line([x + col_w + 6, y0, x + col_w + 6, 388],
                      fill=RULE, width=1)
    draw.line([MARGIN, 394, W - MARGIN, 394], fill=RULE, width=1)


def one_card(draw, story, x, y, w):
    ART[story["art"]](draw, x, y, w, 30)
    chip = "%s %s" % (story["date"], story["mark"])
    cf = font(SANS_BOLD, 8)
    cw = draw.textlength(chip, font=cf) + 8
    draw.rounded_rectangle([x + w - cw - 3, y + 3, x + w - 3, y + 15],
                           radius=5, fill=ACCENT)
    draw.text((x + w - cw + 1, y + 4), chip, font=cf, fill=(255, 255, 255))
    cy = y + 33
    kf, kt = fit_line(draw, "%d · %s" % (story["n"], story["region"].upper()),
                      SANS_BOLD, 8, w)
    draw.text((x, cy), kt, font=kf, fill=REGION_INK[story["region"]])
    cy += 12
    hf, hl = fit_block(draw, story["head"], SERIF_BOLD, 11, w, 3, 8)
    cy = block(draw, hl, hf, x, cy, INK, 13) + 2
    bf, bl = fit_block(draw, story["body"], SANS, 9, w, 2, 7)
    block(draw, bl, bf, x, cy, INK, 11)


def cards_grid(draw):
    gap, y1, y2 = 6, 402, 532
    w6 = (SPAN - 5 * gap) // 6
    for i, story in enumerate(CARDS[:6]):
        one_card(draw, story, MARGIN + i * (w6 + gap), y1, w6)
    for i, story in enumerate(CARDS[6:]):
        one_card(draw, story, MARGIN + i * (w6 + gap), y2, w6)
    draw.line([MARGIN, 662, W - MARGIN, 662], fill=RULE, width=1)


# Rough land boxes (lon_min, lon_max, lat_min, lat_max) for the dot map.
LAND_BOXES = [(-168, -55, 15, 72), (-80, -35, -56, 10), (-11, 32, 36, 70),
              (-18, 51, -35, 35), (32, 180, 5, 77), (95, 141, -11, 5),
              (113, 154, -40, -11), (166, 179, -47, -34)]

# Pins for the fifteen illustrated stories: (number, lon, lat).
PIN_SPOTS = [(1, -100, 40), (2, 107, -6), (3, 21, 52), (4, 20, 32),
             (5, 25, 60), (6, 30, 37), (7, 129, 37), (8, -102, 23),
             (9, 35, 29), (10, 33, 34), (11, 7, 45), (12, 78, 21),
             (13, 6, 46), (14, 140, -20), (15, 51, 35)]


def wire_and_map(draw):
    draw.text((MARGIN, 670), "ALSO — THE REST OF THE DAY, 24 NOVEMBER 2026",
              font=font(SANS_BOLD, 13), fill=INK)
    draw.line([MARGIN, 688, W - MARGIN, 688], fill=RULE, width=1)
    col_w, gap = (SPAN - 2 * 12) // 3, 12
    per = (len(WIRE) + 2) // 3
    for ci in range(3):
        x = MARGIN + ci * (col_w + gap)
        y = 694
        for item in WIRE[ci * per:(ci + 1) * per]:
            label = "%d. %s — %s · %s" % (item["n"], item["head"],
                                          item["region"].upper(),
                                          item["date"])
            fnt, line = fit_line(draw, label, SANS, 9, col_w, 6)
            draw.text((x, y), line, font=fnt, fill=INK)
            y += 19
    # Dotted world map with pins for the illustrated stories.
    mx, my, mw, mh = MARGIN, 844, 470, 104
    draw.text((mx, 830), "WHERE THE DAY HAPPENED — PINS 1–15",
              font=font(SANS_BOLD, 10), fill=INK)
    draw.rectangle([mx, my, mx + mw, my + mh], outline=RULE, width=1)
    for gx in range(mx + 3, mx + mw - 2, 6):
        lon = (gx - mx) / mw * 360 - 180
        for gy in range(my + 3, my + mh - 2, 6):
            lat = 75 - (gy - my) / mh * 135
            if any(a <= lon <= b and c <= lat <= e
                   for a, b, c, e in LAND_BOXES):
                draw.ellipse([gx - 1, gy - 1, gx + 1, gy + 1],
                             fill=(150, 140, 125))
    nf = font(SANS_BOLD, 7)
    for num, lon, lat in PIN_SPOTS:
        px = mx + (lon + 180) / 360 * mw
        py = my + (75 - lat) / 135 * mh
        draw.ellipse([px - 6, py - 6, px + 6, py + 6], fill=ACCENT)
        t = str(num)
        draw.text((px - draw.textlength(t, font=nf) / 2, py - 4), t,
                  font=nf, fill=(255, 255, 255))
    # Region tally, computed from the data so it cannot disagree.
    counts = region_tally()
    order = ["Europe", "Middle East", "N. America", "Latin Am.", "Africa",
             "S. Asia", "E. Asia", "SE Asia & Pacific", "Global"]
    for row, group in enumerate((order[:5], order[5:])):
        tally = "  ·  ".join("%s %d" % (k, counts[k]) for k in group)
        tf, tl = fit_line(draw, ("REGIONS: " if row == 0 else "") + tally,
                          SANS_BOLD, 10, SPAN - 500)
        draw.text((MARGIN + 500, 830 + row * 15), tl, font=tf, fill=INK)
    note = ("Date check: this page is Tuesday 24 November 2026. Fifteen "
            "items carry earlier dates (21–23 Nov) and show them; the "
            "rest happened or were first reported on 24 Nov.")
    nf2, nl = fit_block(draw, note, SANS, 10, SPAN - 500, 4, 8)
    block(draw, nl, nf2, MARGIN + 500, 862, FAINT, 12)


def footer(draw):
    y0 = 970
    draw.rectangle([MARGIN, y0, W - MARGIN, y0 + 24], fill=CARD_BG,
                   outline=ACCENT)
    msg = ("34 STORIES, EACH WITH ITS DATE (15 MARKED 21–23 NOV) · "
           "SOURCES: REUTERS, AP, BLOOMBERG, ESA, FIDE, OXFAM")
    fnt, line = fit_line(draw, msg, SANS_BOLD, 10, SPAN - 16)
    centered(draw, line, fnt, W // 2, y0 + 6, INK)
    centered(draw, "Researched and drawn Tuesday 24 November 2026 · "
                    "One image, one day.",
             font(SANS, 9), W // 2, 1000, FAINT)


def render():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    masthead(draw)
    stats_strip(draw)
    leads_row(draw)
    cards_grid(draw)
    wire_and_map(draw)
    footer(draw)
    return img


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.png")
    render().save(path, format="PNG", optimize=True)
    print("wrote", path, os.path.getsize(path), "bytes,", TOTAL,
          "stories,", len(REGIONS), "regions")


if __name__ == "__main__":
    main()
