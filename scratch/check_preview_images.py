import os
from PIL import Image

p1 = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\assets\services\website-design-preview.jpg"
p2 = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\assets\services\website-design-who-for.webp"
p3 = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\assets\services\website-design-hero-main.webp"

if os.path.exists(p1):
    im1 = Image.open(p1)
    print("website-design-preview.jpg:", im1.size)
if os.path.exists(p2):
    im2 = Image.open(p2)
    print("website-design-who-for.webp:", im2.size)
if os.path.exists(p3):
    im3 = Image.open(p3)
    print("website-design-hero-main.webp:", im3.size)

# Also let's inspect the files in dropbox_photos
db_photos = os.listdir(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\dropbox_photos")
print("Dropbox sample files:", len(db_photos), db_photos[:10])
