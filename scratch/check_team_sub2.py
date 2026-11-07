from PIL import Image

for name, p in [
    ('photo_dec_13', 'assets/lucci/photo_dec_13_2025_2_36_15_pm.jpg'),
    ('top_13', 'assets/archive/top_13.jpg'),
    ('bot_06', 'assets/archive/bot_06.jpg'),
    ('lucci-wide-1', 'assets/lucci/lucci-wide-1.jpg'),
    ('lucci-bts-table', 'assets/lucci/lucci-bts-table.jpg')
]:
    im = Image.open(p)
    w, h = im.size
    print(f"{name:16}: {w}x{h}")
    # sample color
    s = im.resize((10, 10)).convert('RGB')
    pix = list(s.getdata())
    r = sum(x[0] for x in pix)//100
    g = sum(x[1] for x in pix)//100
    b = sum(x[2] for x in pix)//100
    lum = int(0.299*r + 0.587*g + 0.114*b)
    print(f"  RGB: ({r}, {g}, {b})  Lum: {lum}")

