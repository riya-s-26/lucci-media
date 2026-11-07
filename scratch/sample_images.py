import os
from PIL import Image

def get_info(path):
    im = Image.open(path)
    # let's look at corner colors and center colors
    w, h = im.size
    rgb = im.convert('RGB')
    tl = rgb.getpixel((10, 10))
    tr = rgb.getpixel((w - 10, 10))
    bl = rgb.getpixel((10, h - 10))
    br = rgb.getpixel((w - 10, h - 10))
    center = rgb.getpixel((w // 2, h // 2))
    return f"{w}x{h} | corners: {tl},{tr} | center: {center}"

for p in [
    'assets/hero-lex-portrait.jpg',
    'assets/hero-bg.jpg',
    'assets/hero-bg-center.jpg',
    'assets/lucci/lex-portrait-main.jpg',
    'assets/lucci/lex-studio-pose.jpg',
    'assets/lucci/lex-camera-onset.jpg',
    'assets/lucci/lucci-bts-shoot.jpg',
    'assets/lucci/lucci-bts-studio.jpg',
    'assets/lucci/lucci-wide-1.jpg',
    'assets/lucci/lucci-wide-2.jpg',
    'assets/lucci/lucci-wide-3.jpg',
    'assets/product-content.webp',
    'assets/behind-the-lens.webp',
    'assets/on-set.webp',
    'assets/archive/bot_04.jpg',
    'assets/archive/bot_05.jpg',
    'assets/archive/bot_06.jpg',
    'assets/archive/bot_09.jpg',
    'assets/archive/bot_10.jpg',
    'assets/archive/bot_13.jpg',
    'assets/archive/top_01.jpg',
    'assets/archive/top_07.jpg',
    'assets/archive/top_08.jpg',
    'assets/archive/top_11.jpg',
    'assets/archive/top_13.jpg'
]:
    if os.path.exists(p):
        print(f"{p:35}: {get_info(p)}")

