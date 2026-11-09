from PIL import Image

imgs = [
    'assets/about/team_lex.jpg',
    'assets/about/team_studio_chair.jpg',
    'assets/about/team_laptop.jpg',
    'assets/tsa/tsa-team-portrait.jpg',
    'assets/lucci/lucci-bts-shoot.jpg',
    'assets/lucci/lucci-bts-studio.jpg',
    'assets/lucci/lucci-bts-table.jpg',
    'assets/lucci/lex-camera-onset.jpg',
    'assets/lucci/lex-portrait-main.jpg',
    'assets/lucci/photo_dec_13_2025_2_36_15_pm.jpg',
    'assets/lucci/photo_dec_13_2025_3_46_00_pm.jpg'
]

for p in imgs:
    try:
        im = Image.open(p)
        print(f"{p:45} {im.size} {im.mode}")
    except Exception as e:
        print(f"{p:45} ERROR: {e}")

