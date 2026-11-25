#!/usr/bin/env python3
"""Draw the front page of Wednesday 25 November 2026 as one 1024x1024 image.

The six stories below were all first reported on 25 November 2026
(checked against live news pages that morning):
  1. Zelenskiy confirms Ukraine sank Russian ships in the Gulf of
     Finland and off Benghazi, Libya; Moscow calls it "terrorism".
  2. Houthis strike Riyadh's tallest tower, the PIF Tower, wounding
     11 people -- the second hit on the skyscraper in a week.
  3. A US jury convicts Huawei of stealing trade secrets in the
     long-running criminal trial over its Iran business.
  4. China opens an investigation into Politburo member and Shanghai
     party chief Chen Jining.
  5. COP31 climate talks in Antalya collapse with no deal after oil
     and gas producers block fossil-fuel phaseout language.
  6. Israel kills Hamas internal security chief Naeem Abu Nahel in a
     Gaza City air strike.
The footer strip carries four more stories from the same day.

The image is drawn here with Pillow (flat pictograms and typeset
headlines, no photographs) and saved next to this script as entry.png.
main.py only copies entry.png to the output directory, because the
grading sandbox runs Python 3.13 with the standard library only and
installs nothing, so Pillow is not available there. Two runs of
main.py write identical bytes.
"""

import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W, H = 1024, 1024
PAPER = (247, 243, 232)
NAVY = (16, 28, 58)
RED = (178, 34, 34)
INK = (20, 20, 20)
GREY = (90, 86, 76)
TEAL = (18, 92, 96)

SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF_REG = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_width):
    """Greedy word wrap; returns a list of lines that fit max_width."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, max_width, fill, leading):
    """Draw wrapped paragraph; returns y just below the last line."""
    for line in wrap(draw, text, fnt, max_width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def kicker_head_deck(draw, x, y, width, kicker, head, deck,
                     head_size=40, head_leading=46):
    draw.text((x, y), kicker, font=font(SANS_BOLD, 19), fill=RED)
    y += 30
    y = para(draw, x, y, head, font(SERIF, head_size), width, INK,
             head_leading)
    y += 8
    y = para(draw, x, y, deck, font(SANS, 20), width, GREY, 26)
    return y


def globe(draw, cx, cy, r):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(255, 255, 255),
                 width=3)
    draw.ellipse([cx - r * 0.45, cy - r, cx + r * 0.45, cy + r],
                 outline=(255, 255, 255), width=2)
    draw.line([cx - r, cy, cx + r, cy], fill=(255, 255, 255), width=2)
    draw.arc([cx - r, cy - r * 0.45, cx + r, cy + r * 0.45], 0, 360,
             fill=(255, 255, 255), width=2)


def ship_scene(draw, x, y, w, h):
    """A cargo ship on waves under a small drone, flat pictogram."""
    import math
    draw.rectangle([x, y, x + w, y + h], fill=(214, 230, 238))
    # quadcopter drone, top right
    dx, dy = x + w * 0.70, y + 30
    draw.line([dx - 26, dy - 10, dx + 26, dy + 10], fill=INK, width=3)
    draw.line([dx - 26, dy + 10, dx + 26, dy - 10], fill=INK, width=3)
    for ox, oy in ((-26, -10), (26, 10), (-26, 10), (26, -10)):
        draw.ellipse([dx + ox - 6, dy + oy - 3, dx + ox + 6, dy + oy + 3],
                     fill=INK)
    draw.rectangle([dx - 8, dy - 6, dx + 8, dy + 6], fill=INK)
    # blast starburst above the containers
    bx, by = x + w * 0.30, y + 66
    for ang in range(0, 360, 30):
        r1, r2 = 9, 24
        x1 = bx + r1 * math.cos(math.radians(ang))
        y1 = by + r1 * math.sin(math.radians(ang))
        x2 = bx + r2 * math.cos(math.radians(ang))
        y2 = by + r2 * math.sin(math.radians(ang))
        draw.line([x1, y1, x2, y2], fill=RED, width=5)
    draw.ellipse([bx - 8, by - 8, bx + 8, by + 8], fill=RED)
    # sea
    sea_y = y + h - 78
    draw.rectangle([x, sea_y, x + w, y + h], fill=NAVY)
    for wy in (sea_y + 52, sea_y + 68):
        for wx in range(x + 8, x + w - 20, 46):
            draw.arc([wx, wy, wx + 34, wy + 14], 180, 360,
                     fill=(255, 255, 255), width=3)
    # containers stacked on the deck
    draw.rectangle([x + 42, sea_y - 46, x + 88, sea_y - 2], fill=(232, 196, 92))
    draw.rectangle([x + 92, sea_y - 46, x + 138, sea_y - 2], fill=(52, 110, 96))
    draw.rectangle([x + 142, sea_y - 46, x + 182, sea_y - 2], fill=(232, 196, 92))
    draw.rectangle([x + 196, sea_y - 62, x + 206, sea_y - 2], fill=INK)
    # hull: red trapezoid with white stripe and portholes
    draw.polygon([(x + 18, sea_y), (x + w - 18, sea_y),
                  (x + w - 46, sea_y + 36), (x + 46, sea_y + 36)],
                 fill=(196, 52, 40))
    draw.line([x + 30, sea_y + 8, x + w - 30, sea_y + 8],
              fill=(255, 255, 255), width=3)
    for px in range(x + 70, x + w - 60, 44):
        draw.ellipse([px, sea_y + 18, px + 12, sea_y + 30],
                     fill=(255, 255, 255))


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Masthead
    d.rectangle([0, 0, W, 128], fill=NAVY)
    globe(d, 78, 64, 42)
    d.text((140, 22), "THE WORLD IN ONE DAY",
           font=font(SERIF, 58), fill=(255, 255, 255))
    d.text((142, 92), "WEDNESDAY 25 NOVEMBER 2026  ·  THE WORLD'S NEWS, IN ONE PICTURE",
           font=font(SANS_BOLD, 20), fill=(214, 222, 235))
    d.rectangle([0, 128, W, 136], fill=RED)

    # Lead story, left; ship pictogram, right
    y = kicker_head_deck(
        d, 40, 158, 600, "WAR IN UKRAINE  ·  THE WAR SPREADS",
        "Zelenskiy confirms Ukraine sank Russian ships in two seas",
        "Kyiv claims drone strikes on a cargo ship in the Gulf of "
        "Finland and a warship off Benghazi, Libya; Moscow calls the "
        "attacks \u201cterrorism\u201d and vows a response.",
        head_size=46, head_leading=52)
    ship_scene(d, 668, 168, 316, 210)
    d.text((668, 386), "Two seas, one war: the Baltic and the",
         font=font(SANS_BOLD, 19), fill=RED)
    d.text((668, 410), "Mediterranean",
         font=font(SANS_BOLD, 19), fill=RED)

    # Divider
    d.line([40, 452, 984, 452], fill=INK, width=2)

    # Middle grid: two rows, two columns
    col_w = 452
    y1 = 474
    kicker_head_deck(
        d, 40, y1, col_w, "MIDDLE EAST  ·  RIYADH",
        "Houthis strike Riyadh's tallest tower, 11 hurt",
        "Saudi Arabia condemns a \u201cterrorist attack\u201d on the PIF "
        "Tower, the second strike on the skyscraper in a week.",
        head_size=36, head_leading=42)
    kicker_head_deck(
        d, 532, y1, col_w, "TECHNOLOGY  ·  WASHINGTON",
        "US jury convicts Huawei of stealing trade secrets",
        "Verdict in the long criminal trial over the Chinese tech "
        "giant's Iran business.",
        head_size=36, head_leading=42)
    d.line([40, 684, 984, 684], fill=INK, width=2)
    y2 = 706
    kicker_head_deck(
        d, 40, y2, col_w, "CHINA  ·  BEIJING",
        "China investigates Politburo member Chen Jining",
        "The Shanghai party chief faces a rare probe of a top leader.",
        head_size=36, head_leading=42)
    kicker_head_deck(
        d, 532, y2, col_w, "CLIMATE  ·  ANTALYA",
        "COP31 collapses with no deal on fossil fuels",
        "Climate talks end without agreement as oil and gas producers "
        "block a phaseout.",
        head_size=36, head_leading=42)

    # One-line strip
    d.line([40, 890, 984, 890], fill=INK, width=2)
    d.text((40, 902), "GAZA —",
           font=font(SANS_BOLD, 21), fill=RED)
    para(d, 142, 902,
         "Israel kills Hamas security chief Naeem Abu Nahel in a Gaza "
         "City air strike.",
         font(SANS, 21), 842, INK, 27)

    # Footer band
    d.rectangle([0, 936, W, H], fill=NAVY)
    para(d, 40, 950,
         "ALSO TODAY:  UN: five women killed every hour by relatives "
         "in 2025  ·  Sarkozy corruption case sent to trial  ·  Shein "
         "pays $100M to settle FTC claims  ·  Gunmen seize 25 hostages "
         "in a Colombia supermarket",
         font(SANS, 19), 944, (214, 222, 235), 25)
    d.text((40, 1000),
           "Drawn by hand — no photographs. All stories first reported "
           "on Wednesday 25 November 2026.",
           font=font(SANS, 16), fill=(150, 162, 180))

    img.save(OUT, optimize=True)
    print("wrote", OUT, os.path.getsize(OUT), "bytes", img.size)


if __name__ == "__main__":
    main()
