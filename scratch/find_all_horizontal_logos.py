import os
from PIL import Image

for root, dirs, files in os.walk('.'):
    if '.git' in root: continue
    for f in files:
        if f.lower().endswith(('.png', '.jpg', '.webp')):
            p = os.path.join(root, f)
            try:
                im = Image.open(p)
                ar = im.width / im.height
                if 6.0 <= ar <= 8.5:
                    print(f"{p:50} {im.size} AR: {ar:.2f}")
            except:
                pass

