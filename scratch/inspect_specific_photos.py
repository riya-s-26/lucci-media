import os
from PIL import Image

db_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\dropbox_photos"

for fname in ["IMG_8364.jpg", "IMG_0020.JPG", "IMG_0021.JPG", "IMG_9979.JPG"]:
    p = os.path.join(db_dir, fname)
    im = Image.open(p)
    print(f"{fname}: {im.size}")
