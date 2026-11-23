import os
from PIL import Image

db_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\dropbox_photos"
files = [f for f in os.listdir(db_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]

print(f"Total files: {len(files)}")
catalog = []
for f in files:
    p = os.path.join(db_dir, f)
    im = Image.open(p)
    catalog.append((f, im.size, os.path.getsize(p)))

for item in catalog:
    print(f"{item[0]}: {item[1][0]}x{item[1][1]} ({item[2]} bytes)")
