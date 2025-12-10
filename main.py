"""Christmas themed 8x8 slideshow for Cosmic Unicorn."""

from cosmic import CosmicUnicorn
from picographics import PicoGraphics, DISPLAY_COSMIC_UNICORN
import time

# ---------- Canonical colors ----------
COLORS = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "snow": (235, 245, 255),
    "sky": (80, 140, 200),
    "gold": (255, 210, 60),
    "red": (220, 40, 50),
    "green_tree": (20, 140, 60),
    "brown_trunk": (110, 60, 20),
    "orange": (240, 130, 40),
    "gift_blue": (40, 140, 200),
    "pink_ribbon": (240, 120, 170),
}

# ---------- Artworks ----------
# Each artwork provides:
# - grid: list of 8 strings x 8 chars
# - legend: maps letters used in grid -> canonical color names (keys in COLORS)
ARTWORKS = [
    {
        "name": "Christmas Tree",
        "legend": {
            "A": "sky",
            "T": "green_tree",
            "O": "red",
            "S": "gold",
            "B": "brown_trunk",
        },
        "grid": [
            "AAASAAAA",
            "AAATTAAA",
            "AATTTTAA",
            "AATOTTAA",
            "ATTTTTTA",
            "ATTOOTTA",
            "AAABBBAA",
            "AAABBBAA",
        ],
    },
    {
        "name": "Snowman",
        "legend": {
            "A": "sky",
            "H": "black",
            "W": "snow",
            "K": "black",
            "O": "orange",
        },
        "grid": [
            "AAHHHAAA",
            "AAHHHAAA",
            "AAWKWAAA",
            "AWWOWWAA",
            "AWWWWWWA",
            "AWWKWWWA",
            "AWWKWWWA",
            "AAWWWWAA",
        ],
    },
    {
        "name": "Gift Box",
        "legend": {
            "A": "sky",
            "B": "gift_blue",
            "R": "pink_ribbon",
        },
        "grid": [
            "AAAAAAAA",
            "AABBBBAA",
            "AABBBBAA",
            "AARRRRAA",
            "AARRRRAA",
            "AABRRBAA",
            "AABRRBAA",
            "AABRRBAA",
        ],
    },
]

# ---------- Setup ----------
cu = CosmicUnicorn()
g = PicoGraphics(display=DISPLAY_COSMIC_UNICORN)
cu.set_brightness(0.45)

SCALE = 4  # 32 / 8
art_index = 0
slide_seconds = 2.0
last_switch = time.time()

def color_from_letter(letter: str, legend: dict):
    """Resolve a letter to an RGB tuple via legend -> COLORS.
       Fallback to black if anything is missing."""
    name = legend.get(letter)
    return COLORS.get(name, (0, 0, 0))

def draw_art(art):
    g.set_pen(g.create_pen(0, 0, 0))
    g.clear()

    legend = art.get("legend", {})
    grid = art["grid"]

    # basic validation (optional)
    if len(grid) != 8 or any(len(row) != 8 for row in grid):
        # If invalid, just don't crash—show blank.
        cu.update(g)
        return

    for y in range(8):
        row = grid[y]
        for x in range(8):
            r, gg, b = color_from_letter(row[x], legend)
            g.set_pen(g.create_pen(r, gg, b))
            g.rectangle(x * SCALE, y * SCALE, SCALE, SCALE)

    cu.update(g)

# ---------- Loop ----------
draw_art(ARTWORKS[art_index])
while True:
    if time.time() - last_switch >= slide_seconds:
        art_index = (art_index + 1) % len(ARTWORKS)
        draw_art(ARTWORKS[art_index])
        last_switch = time.time()
    time.sleep(0.05)
