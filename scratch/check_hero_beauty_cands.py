from PIL import Image

candidates = {
    'bts_shoot': 'assets/lucci/lucci-bts-shoot.jpg',
    'product_content': 'assets/product-content.webp',
    'top_01_beauty_campaign': 'assets/archive/top_01.jpg',
    'camera_onset': 'assets/lucci/lex-camera-onset.jpg',
    'bot_04_treatment_shoot': 'assets/archive/bot_04.jpg',
    'brown_sugar_skin': 'assets/brown-sugar-skin.webp',
    'top_06_onset': 'assets/archive/top_06.jpg',
}

for name, path in candidates.items():
    im = Image.open(path)
    w, h = im.size
    print(f"{name:25} {w}x{h} ({w/h:.2f})")

