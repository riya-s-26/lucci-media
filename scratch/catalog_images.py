import os
from PIL import Image

def analyze(path):
    try:
        im = Image.open(path)
        w, h = im.size
        # average color
        rgb = im.convert('RGB')
        s = rgb.resize((30, 30))
        pix = list(s.getdata())
        r = sum(p[0] for p in pix) // len(pix)
        g = sum(p[1] for p in pix) // len(pix)
        b = sum(p[2] for p in pix) // len(pix)
        lum = int(0.299*r + 0.587*g + 0.114*b)
        return w, h, (r, g, b), lum
    except Exception as e:
        return None

print("=== ASSETS / LUCCI ===")
for f in os.listdir('assets/lucci'):
    p = os.path.join('assets/lucci', f)
    res = analyze(p)
    if res:
        print(f"{f:30} {res[0]}x{res[1]} RGB:{res[2]} Lum:{res[3]}")

print("\n=== ASSETS (root) ===")
for f in os.listdir('assets'):
    p = os.path.join('assets', f)
    if os.path.isfile(p):
        res = analyze(p)
        if res:
            print(f"{f:30} {res[0]}x{res[1]} RGB:{res[2]} Lum:{res[3]}")

print("\n=== ASSETS / ARCHIVE ===")
for f in sorted(os.listdir('assets/archive')):
    p = os.path.join('assets/archive', f)
    res = analyze(p)
    if res:
        print(f"{f:30} {res[0]}x{res[1]} RGB:{res[2]} Lum:{res[3]}")

