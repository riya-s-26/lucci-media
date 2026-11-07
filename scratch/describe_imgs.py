from PIL import Image

imgs = {
    'about_portrait.jpg': 'assets/about/about_portrait.jpg',
    'founder-lex.webp': 'assets/founder-lex.webp',
    'hero-lex-portrait.jpg': 'assets/hero-lex-portrait.jpg',
    'lex-studio-pose.jpg': 'assets/lucci/lex-studio-pose.jpg',
    'lex-portrait-main.jpg': 'assets/lucci/lex-portrait-main.jpg',
    'lucci-bts-shoot.jpg': 'assets/lucci/lucci-bts-shoot.jpg',
    'lucci-wide-1.jpg': 'assets/lucci/lucci-wide-1.jpg',
    'lucci-wide-2.jpg': 'assets/lucci/lucci-wide-2.jpg',
    'product-content.webp': 'assets/product-content.webp',
    'brown-sugar-skin.webp': 'assets/brown-sugar-skin.webp',
}

for name, path in imgs.items():
    im = Image.open(path)
    print(f"=== {name} ({im.size}) ===")
    # let's sample 5 vertical slices
    w, h = im.size
    rgb = im.convert('RGB')
    s = rgb.resize((10, 10))
    p = list(s.getdata())
    r = sum(x[0] for x in p)//100
    g = sum(x[1] for x in p)//100
    b = sum(x[2] for x in p)//100
    print(f"Average color: ({r}, {g}, {b})")

