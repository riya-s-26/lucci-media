import os
from PIL import Image

db_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\dropbox_photos"
files = [f for f in os.listdir(db_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]

# Let's inspect some of the high-res DSC and IMG files to see their colors and features
for f in files:
    p = os.path.join(db_dir, f)
    im = Image.open(p)
    w, h = im.size
    aspect = "horizontal" if w > h else "vertical"
    # sample average color
    thumb = im.resize((1, 1)).getpixel((0, 0))
    print(f"{f:38} | {w:4}x{h:4} | {aspect:10} | avg_rgb: {thumb}")
