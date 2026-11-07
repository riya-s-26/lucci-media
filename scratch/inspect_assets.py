import os
from PIL import Image

def analyze_img(path):
    try:
        with Image.open(path) as img:
            w, h = img.size
            mode = img.mode
            img_rgb = img.convert('RGB')
            # sample colors
            small = img_rgb.resize((50, 50))
            pixels = list(small.getdata())
            r_avg = sum(p[0] for p in pixels) / len(pixels)
            g_avg = sum(p[1] for p in pixels) / len(pixels)
            b_avg = sum(p[2] for p in pixels) / len(pixels)
            brightness = (r_avg * 299 + g_avg * 587 + b_avg * 114) / 1000
            return (w, h, round(r_avg), round(g_avg), round(b_avg), round(brightness))
    except Exception as e:
        return str(e)

for folder in ['assets', 'assets/about', 'assets/lucci', 'assets/archive', 'assets/services']:
    if os.path.exists(folder):
        print(f"\n--- {folder} ---")
        for f in os.listdir(folder):
            if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
                full_path = os.path.join(folder, f)
                res = analyze_img(full_path)
                print(f"{f:35} {str(res)}")

