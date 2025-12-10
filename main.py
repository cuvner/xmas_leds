# Cosmic Unicorn 8×8 slideshow with a canonical color library + per-art legends
from cosmic import CosmicUnicorn
from picographics import PicoGraphics, DISPLAY_COSMIC_UNICORN
import time

# ---------- Canonical colors (no repeats here) ----------
COLORS = {
    "black":     (0, 0, 0),
    "white":     (255, 255, 255),
    "yellow":    (255, 255, 0),
    "red":       (255, 0, 0),
    "green":     (40, 160, 60),
    "blue":      (0, 80, 200),
    "darkgrey":  (130, 130, 130),
    "lightgrey": (185, 185, 185),
    "cyan":      (0, 255, 255),
    "brown_dark":(120, 70, 20),
    "brown_orange": (160, 90, 20),
    "blue_l": (96, 128, 224),
    "blue_d": (64, 96, 192),
    "yellow": (224, 224, 96),
    "orange": (224, 128, 64),
    "gold": (224, 192, 64),
    "white_soft": (224, 224, 224),
    "green_neon": (0, 224, 96),
    "purple_vivid": (96, 0, 224),
    "purple_d": (64, 0, 96),
    "gray_m": (128, 128, 128),
    "gray_d": (64, 64, 64),
    "yellow": (224, 224, 96),
    "orange": (224, 128, 64),
    "red_bright": (224, 0, 32),
    "green_m": (32, 160, 96),
    "green_dd": (0, 64, 32),
    "green_d": (0, 96, 32),
    "green_neon": (0, 224, 96),
    "purple_d": (64, 32, 192),
    "purple_vivid": (96, 0, 224),
    "red_dark": (128, 0, 0),
    "white_soft": (224, 224, 224),
    "green_alien": (0, 255, 128),
    "black": (0, 0, 0),
    "yellow_bright": (255, 255, 128),
    "green_tree": (0, 96, 32),
    "green_leaf": (64, 192, 96),
    "orange": (255, 160, 64),
    "brown_trunk": (96, 0, 0),
    "green_neon": (0, 224, 96),
    "purple": (128, 0, 255),
    "sky": (128, 160, 224),
    "tree_green": (0, 128, 64),
    "yellow_bright": (255, 255, 128),
    "brown": (128, 64, 0),
    "sand": (255, 224, 160),
    "red": (224, 0, 0),
    "grass_m": (0, 160, 96),


    






    # landscape set
    "sky":       (150, 200, 210),
    "grass_d":   (20, 80, 30),
    "grass_m":   (50, 140, 50),
    "dirt":      (120, 60, 0),
    "moss":      (100, 180, 90),
}

# ---------- Artworks ----------
# Each artwork provides:
# - grid: list of 8 strings x 8 chars
# - legend: maps letters used in grid -> canonical color NAMES (keys in COLORS)
ARTWORKS = [
    {
        "name": "Smiley",
        "legend": {"Y": "yellow", "B": "black", "R": "red"},
        "grid": [
            "YYYYYYYY",
            "YYBYYBYY",
            "YYYYYYYY",
            "YRYYYRYY",
            "YYYYYYYY",
            "YYBYYBYY",
            "YYBBBBYY",
            "YYYYYYYY",
        ],
    },
    {
    "name": "BlueGrey Frame",
    "legend": {"B": "blue", "Y": "yellow", "W": "white", "L": "lightgrey", "D": "darkgrey"},
    "grid": [
        "YBBBYBBB",
        "BBWWWLBY",
        "BWWDWWLB",
        "BLLWWWWB",
        "BWWDDWWB",
        "YWDWWWWB",
        "BBBWLWBB",
        "BBBYBBBY",
    ],
},
    {
    "name": "Beaver",
    "legend": {
        "C": "cyan",
        "B": "brown_dark",
        "O": "brown_orange",
        "K": "black",
        "W": "white",
    },
    "grid": [
        "CCCCCCCC",
        "CCBBBCCC",
        "CBBBBBBB",
        "CBKBBKBB",
        "COOOOOBB",   # <- 8 chars (C + O*5 + B + C)
        "CCWBBWBB",
        "CCWBBWBB",
        "OBWBBWBB",
    ],
},
    {
        "name": "Landscape",
        "legend": {"S": "sky", "D": "grass_d", "M": "grass_m", "H": "black", "T": "dirt", "O": "moss"},
        "grid": [
            "SSDDDSSS",
            "SDDDDSSS",
            "MHMMMMMS",
            "MMMMMMMM",
            "TTOTTOTO",
            "SSSSSSSO",
            "SSSSDSSM",
            "SSSSSDDM",
        ],
    },
    {
        "name": "Blue/Grey Frame",
        "legend": {"B": "blue", "Y": "yellow", "W": "white", "L": "lightgrey", "D": "darkgrey"},
        "grid": [
            "YBBBYBBB",
            "BBWWWWLB",
            "BWWDWWLB",
            "BLLWWWWB",
            "BWWDDWWB",
            "YWDWWWWB",
            "BBBWLWBB",
            "BBBYBBBY",
        ],
    },

    {
    "name": "Tree_Landscape",
    "legend": {
        "S": "sky",
        "G": "tree_green",
        "Y": "yellow_bright",
        "B": "brown",
        "A": "sand",
        "R": "red",
        "M": "grass_m"
    },
    "grid": [
        "SGGGSSYY",
        "SGGGSSSS",
        "SSGSSSSS",
        "BBBSSAYS",
        "BBBSARMS",
        "MMMMMMMM",
        "MMMMMMMM",
        "MMMMMMMM",
    ],
},
    {
    "name": "Tree",
    "legend": {
        "Y": "yellow_bright",
        "T": "green_tree",
        "L": "green_leaf",
        "O": "orange",
        "B": "brown_trunk",
        "N": "green_neon",
        "P": "purple",
        "K": "black"
    },
    "grid": [
        "YTTTTLYO",
        "OLTTTLOO",
        "YOYTLTOY",
        "OOBBBOOO",
        "KKNNNPKK",
        "KPPNPPPK",
        "KPNNPNPK",
        "KPPNPPPK",
    ],
},
{
    "name": "Alien_Face",
    "legend": {
        "G": "green_alien",
        "K": "black",
        "W": "white"
    },
    "grid": [
        "KGKGKGKG",
        "GGGGGGGG",
        "GWKWKWKG",
        "GGGGGGGG",
        "GGGGGGGG",
        "GGGGGGGG",
        "GGKKKKGG",
        "KGGGGGGK",
    ],
},
    {
    "name": "Frog_Pond",
    "legend": {
        "A": "white_soft",
        "B": "green_d",
        "C": "green_neon",
        "D": "red_dark",
        "E": "green_dd",
        "F": "purple_vivid",
        "G": "purple_d",
    },
    "grid": [
        "ABCBBBBA",
        "BBDCBCBB",
        "EEDBCDCE",
        "FFGEFDFF",
        "GGGGGGGG",
        "EGFFGGEG",
        "CEEEECBE",
        "ADDBCDCA",
    ],
},
    {
    "name": "Rocket",
    "legend": {
        "A": "purple_d",
        "B": "gray_m",
        "C": "gray_d",
        "D": "yellow",
        "E": "green_m",
        "F": "orange",
        "G": "red_bright",
    },
    "grid": [
        "AAABBAAA",
        "AABCCBAA",
        "AABCCBAA",
        "AABBBBAA",
        "ABBBBBBA",
        "ADDDDDDA",
        "EEFFFFEE",
        "EEEGGEEE",
    ],
},
    {
    "name": "Pixel_Flower",
    "legend": {
        "A": "black",
        "B": "white_soft",
        "C": "green_neon",
        "D": "purple_vivid",
    },
    "grid": [
        "ABABAAAA",
        "AAAAAABA",
        "BAACDAAA",
        "AACDCDAB",
        "BADCDDAA",
        "AAADCAAA",
        "ABAAAABA",
        "AAAAAAAA",
    ],
},
    {
    "name": "Chick",
    "legend": {
        "A": "blue_l",
        "B": "blue_d",
        "C": "yellow",
        "D": "black",
        "E": "orange",
        "F": "gold",
    },
    "grid": [
        "ABBBBBBB",
        "ACCCCCBB",
        "ACDCCCBB",
        "ECCCCFFB",
        "ACCCFFFB",
        "ACCFFFBB",
        "ACCCCCBB",
        "AAAEEBBB",
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




