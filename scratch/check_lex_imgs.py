import os
from PIL import Image

def describe_img(path):
    im = Image.open(path)
    print(f"Path: {path}, Size: {im.size}, Format: {im.format}")

for root, dirs, files in os.walk('assets'):
    for f in files:
        if 'about' in f.lower() or 'portrait' in f.lower() or 'lex' in f.lower():
            p = os.path.join(root, f)
            if p.lower().endswith(('.jpg', '.png', '.webp')):
                describe_img(p)

