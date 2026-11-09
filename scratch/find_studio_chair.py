import os
from PIL import Image

# Search all jpg/webp files across workspace to see if any contain the chair or studio
for root, dirs, files in os.walk('assets'):
    for f in files:
        if f.endswith(('.jpg', '.webp')):
            p = os.path.join(root, f)
            try:
                im = Image.open(p)
                # check aspect ratio around 1.6 (1200x750)
                ar = im.width / im.height
                if 1.5 <= ar <= 1.7:
                    print(f"{p:50} {im.size}  AR: {ar:.2f}")
            except:
                pass

