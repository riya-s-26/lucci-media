import os
from PIL import Image

# Let's inspect the images in detail
# We can check specific pixel regions to understand what they are
def analyze_scene(name, path):
    im = Image.open(path)
    w, h = im.size
    print(f"\n--- {name} ({w}x{h}) ---")
    # Sample top-left, top-right, center, bottom-left, bottom-right
    samples = {
        'TL': im.getpixel((w//6, h//6)),
        'TR': im.getpixel((5*w//6, h//6)),
        'C':  im.getpixel((w//2, h//2)),
        'BL': im.getpixel((w//6, 5*h//6)),
        'BR': im.getpixel((5*w//6, 5*h//6))
    }
    for k, v in samples.items():
        print(f"  {k}: {v}")

db_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\dropbox_photos"
for f in ["IMG_0020.JPG", "IMG_0021.JPG", "IMG_4088.JPG", "DSC00336.JPG", "DSC08037.JPG", "IMG_8364.jpg", "IMG_9960.JPG", "IMG_9983.JPG"]:
    analyze_scene(f, os.path.join(db_dir, f))
