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
if hasattr(cu, "set_volume"):
    # keep the melody gentle so it accompanies the lights
    try:
        cu.set_volume(0.35)
    except Exception:
        pass

SCALE = 4  # 32 / 8
art_index = 0
slide_seconds = 2.0
last_switch = time.time()
melody_index = 0
next_note_time = time.time()

# Jingle-style melody (Hz, seconds). A frequency of 0.0 is a rest.
MELODY = [
    (659, 0.35),  # E5
    (659, 0.35),
    (659, 0.7),
    (659, 0.35),
    (659, 0.35),
    (659, 0.7),
    (659, 0.35),
    (783, 0.35),  # G5
    (523, 0.35),  # C5
    (587, 0.35),  # D5
    (659, 0.9),
    (0.0, 0.25),  # breath
    (698, 0.35),  # F5
    (698, 0.35),
    (698, 0.35),
    (698, 0.35),
    (698, 0.35),
    (659, 0.35),
    (659, 0.35),
    (659, 0.2),
    (659, 0.2),
    (659, 0.35),
    (587, 0.35),
    (587, 0.35),
    (659, 0.35),
    (587, 0.35),
    (783, 0.9),
]

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


def play_note(frequency_hz: float, duration_s: float, volume: float = 0.45):
    """Best-effort tone playback that adapts to available Cosmic Unicorn APIs."""
    if frequency_hz <= 0 or duration_s <= 0:
        return

    # Prefer a dedicated tone helper if it exists.
    if hasattr(cu, "play_tone"):
        try:
            cu.play_tone(frequency_hz, duration_s, volume)
            return
        except Exception:
            pass

    # Fallback to a synth-style API that may accept ADSR params.
    if hasattr(cu, "play_note"):
        try:
            cu.play_note(frequency_hz, duration_s, volume)
            return
        except Exception:
            pass


def advance_melody(now: float):
    """Schedule the next note in the background melody."""
    global melody_index, next_note_time

    if now < next_note_time:
        return

    frequency, beat = MELODY[melody_index]
    play_note(frequency, beat)

    melody_index = (melody_index + 1) % len(MELODY)
    next_note_time = now + beat

# ---------- Loop ----------
draw_art(ARTWORKS[art_index])
while True:
    now = time.time()
    advance_melody(now)

    if now - last_switch >= slide_seconds:
        art_index = (art_index + 1) % len(ARTWORKS)
        draw_art(ARTWORKS[art_index])
        last_switch = now
    time.sleep(0.05)
