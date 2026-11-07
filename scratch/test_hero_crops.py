from PIL import Image

for name, src in [
    ('lex-studio-pose', 'assets/lucci/lex-studio-pose.jpg'),
    ('hero-lex-portrait', 'assets/hero-lex-portrait.jpg'),
    ('hero-bg-center', 'assets/hero-bg-center.jpg')
]:
    im = Image.open(src)
    w, h = im.size
    # Target 16:10
    target_ratio = 16 / 10
    # if image is portrait (h > w), crop height to match w / target_ratio
    crop_h = int(w / target_ratio)
    # let's try focusing on top/mid where Lex's face and torso are (e.g. from y=0 to y=crop_h or y=0.1*h to y=0.1*h+crop_h)
    start_y = int(h * 0.05)
    box = (0, start_y, w, start_y + crop_h)
    crop = im.crop(box)
    crop_small = crop.resize((40, 25)).convert('RGB')
    pix = list(crop_small.getdata())
    r = sum(p[0] for p in pix) // len(pix)
    g = sum(p[1] for p in pix) // len(pix)
    b = sum(p[2] for p in pix) // len(pix)
    lum = int(0.299*r + 0.587*g + 0.114*b)
    print(f"{name} 16:10 crop: RGB=({r},{g},{b}), Lum={lum}")

