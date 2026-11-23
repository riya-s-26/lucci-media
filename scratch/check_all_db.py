import os
from PIL import Image

db_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\dropbox_photos"
files = [f for f in os.listdir(db_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]

# Let's inspect some of the files and see their descriptions
# We can create a script that crops a small center patch of each and gives info
for f in files:
    p = os.path.join(db_dir, f)
    im = Image.open(p)
    w, h = im.size
    print(f"File: {f} | {w}x{h}")
