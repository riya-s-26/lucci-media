import os
from PIL import Image

db_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\dropbox_photos"
out_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\horizontal_samples"
os.makedirs(out_dir, exist_ok=True)

horizontals = [
    "IMG_0020.JPG", "IMG_0021.JPG", "IMG_0217 (1).JPG", "IMG_4088.JPG",
    "IMG_9808.JPG", "IMG_9960.JPG", "IMG_9969.JPG", "IMG_9979.JPG",
    "IMG_9983.JPG", "DSC00336.JPG", "DSC02158.JPG", "DSC03284.JPG",
    "DSC05857.JPG", "DSC05862.JPG", "DSC08037.JPG", "Tezza-3818.jpg"
]

print("Processing horizontal samples...")
for h in horizontals:
    p = os.path.join(db_dir, h)
    im = Image.open(p)
    im_thumb = im.copy()
    im_thumb.thumbnail((400, 300))
    im_thumb.convert('RGB').save(os.path.join(out_dir, f"sample_{h}.jpg"), quality=80)
    print(f"  {h}: saved sample")

print("Done!")
