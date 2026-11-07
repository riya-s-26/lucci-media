from PIL import Image

for name, path in [
    ('lex-studio-pose', 'assets/lucci/lex-studio-pose.jpg'),
    ('hero-lex-portrait', 'assets/hero-lex-portrait.jpg'),
    ('hero-bg-center', 'assets/hero-bg-center.jpg'),
    ('founder-lex', 'assets/founder-lex.webp'),
    ('about_portrait', 'assets/about/about_portrait.jpg'),
]:
    im = Image.open(path)
    w, h = im.size
    # let's look at top 10% (background behind head), center 50% (face/torso), bottom 20%
    top = im.crop((0, 0, w, int(h*0.15))).convert('RGB').resize((5, 5))
    top_c = [sum(x[i] for x in top.getdata())//25 for i in range(3)]
    mid = im.crop((int(w*0.25), int(h*0.2), int(w*0.75), int(h*0.7))).convert('RGB').resize((5, 5))
    mid_c = [sum(x[i] for x in mid.getdata())//25 for i in range(3)]
    bot = im.crop((0, int(h*0.8), w, h)).convert('RGB').resize((5, 5))
    bot_c = [sum(x[i] for x in bot.getdata())//25 for i in range(3)]
    print(f"=== {name} ({w}x{h}) ===")
    print(f"  Top background: {top_c}")
    print(f"  Mid subject: {mid_c}")
    print(f"  Bottom: {bot_c}")

