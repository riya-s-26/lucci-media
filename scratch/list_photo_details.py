import os
import glob
from PIL import Image

db_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\dropbox_photos"

# Let's inspect each photo and print some info
photos = [f for f in os.listdir(db_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]

# Let's check which ones have high resolution and good med spa / clinic context
for f in photos:
    p = os.path.join(db_dir, f)
    im = Image.open(p)
    w, h = im.size
    print(f"{f:35} | {w}x{h} | {os.path.getsize(p)//1024}KB")
