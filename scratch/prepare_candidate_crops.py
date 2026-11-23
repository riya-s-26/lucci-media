import os
from PIL import Image

db_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\dropbox_photos"
out_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\gbp_candidates"
os.makedirs(out_dir, exist_ok=True)

candidates = [
    "IMG_0020.JPG", "IMG_0021.JPG", "DSC08037.JPG", "DSC00336.JPG", 
    "IMG_4088.JPG", "IMG_9983.JPG", "DSC05862.JPG", "IMG_8364.jpg",
    "IMG_9960.JPG", "DSC02158.JPG", "DSC03284.JPG", "IMG_0217 (1).JPG"
]

print("Generating candidate crops...")
for c in candidates:
    p = os.path.join(db_dir, c)
    im = Image.open(p)
    w, h = im.size
    
    # Let's crop to 16:10 or 4:3 for hero / who-it's-for preview
    if w > h:
        # horizontal: crop center
        target_h = int(w * 0.7)
        if target_h <= h:
            top = (h - target_h) // 2
            crop = im.crop((0, top, w, top + target_h))
        else:
            target_w = int(h / 0.7)
            left = (w - target_w) // 2
            crop = im.crop((left, 0, left + target_w, h))
    else:
        # vertical: crop top-center
        target_h = int(w * 0.75)
        top = int(h * 0.15)
        crop = im.crop((0, top, w, min(h, top + target_h)))
    
    crop_thumb = crop.resize((540, 380), Image.Resampling.LANCZOS)
    crop_thumb.convert('RGB').save(os.path.join(out_dir, f"crop_{c}.jpg"), quality=85)
    print(f"  Saved crop_{c}.jpg")

print("Candidate crops ready!")
