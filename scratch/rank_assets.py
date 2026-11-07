import os
from PIL import Image

def analyze_full(path):
    im = Image.open(path)
    w, h = im.size
    rgb = im.convert('RGB')
    s = rgb.resize((50, 50))
    pix = list(s.getdata())
    r = sum(p[0] for p in pix) / len(pix)
    g = sum(p[1] for p in pix) / len(pix)
    b = sum(p[2] for p in pix) / len(pix)
    lum = 0.299*r + 0.587*g + 0.114*b
    
    # check if tones are warm (r >= g >= b or warm beige/ivory)
    is_warm = (r >= b) and (r >= 150 and g >= 140 and b >= 130)
    
    # percentage of very dark pixels (< 50 lum)
    dark_pix = sum(1 for p in pix if (0.299*p[0] + 0.587*p[1] + 0.114*p[2]) < 50)
    dark_pct = (dark_pix / len(pix)) * 100
    
    return {
        'path': path,
        'size': (w, h),
        'rgb': (round(r), round(g), round(b)),
        'lum': round(lum),
        'is_warm': is_warm,
        'dark_pct': round(dark_pct, 1)
    }

candidates = []
for folder in ['assets', 'assets/lucci', 'assets/archive']:
    for f in os.listdir(folder):
        p = os.path.join(folder, f)
        if os.path.isfile(p) and p.lower().endswith(('.jpg', '.jpeg', '.webp')):
            res = analyze_full(p)
            candidates.append(res)

# Sort by luminance descending
candidates.sort(key=lambda x: x['lum'], reverse=True)

print(f"{'Filename':40} {'Size':15} {'Lum':5} {'Dark%':6} {'Warm?':6} {'RGB'}")
print("-" * 85)
for c in candidates:
    fname = os.path.relpath(c['path'])
    print(f"{fname:40} {str(c['size']):15} {c['lum']:<5} {c['dark_pct']:<6} {str(c['is_warm']):<6} {c['rgb']}")

