# Let's inspect the images in detail by printing their dominant colors, aspect ratios, and visual composition
from PIL import Image

def inspect_details(name, p):
    im = Image.open(p)
    w, h = im.size
    print(f"=== {name} ===")
    print(f"  Aspect Ratio: {w/h:.2f} ({w}x{h})")
    # center crop color
    cw, ch = w//4, h//4
    box = (w//2 - cw//2, h//2 - ch//2, w//2 + cw//2, h//2 + ch//2)
    crop = im.crop(box).convert('RGB')
    s = crop.resize((10, 10))
    pix = list(s.getdata())
    r = sum(x[0] for x in pix)//100
    g = sum(x[1] for x in pix)//100
    b = sum(x[2] for x in pix)//100
    print(f"  Center region RGB: ({r}, {g}, {b})")

inspect_details("lex-studio-pose", "assets/lucci/lex-studio-pose.jpg")
inspect_details("hero-lex-portrait", "assets/hero-lex-portrait.jpg")
inspect_details("product-content", "assets/product-content.webp")
inspect_details("brown-sugar-skin", "assets/brown-sugar-skin.webp")
inspect_details("lucci-bts-shoot", "assets/lucci/lucci-bts-shoot.jpg")
inspect_details("archive top_01", "assets/archive/top_01.jpg")
inspect_details("archive top_08", "assets/archive/top_08.jpg")
inspect_details("archive top_13", "assets/archive/top_13.jpg")
inspect_details("archive bot_04", "assets/archive/bot_04.jpg")
inspect_details("archive bot_05", "assets/archive/bot_05.jpg")
inspect_details("archive bot_06", "assets/archive/bot_06.jpg")
inspect_details("archive bot_07", "assets/archive/bot_07.jpg")
inspect_details("archive bot_09", "assets/archive/bot_09.jpg")
inspect_details("archive bot_10", "assets/archive/bot_10.jpg")
inspect_details("archive bot_13", "assets/archive/bot_13.jpg")

