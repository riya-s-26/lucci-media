import os
import glob
import re
from PIL import Image

base_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media"
db_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\dropbox_photos"

# 1. Check images used in Services 1-6
service_files = [
    "social-media-management-boston.html",
    "beauty-content-creation-boston.html",
    "brand-photography-boston.html",
    "beauty-campaign-production.html",
    "beauty-brand-identity-design.html",
    "med-spa-website-design.html"
]

used_images = set()
for sf in service_files:
    p = os.path.join(base_dir, sf)
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            c = f.read()
        # Find all img src and srcset
        imgs = re.findall(r'src=["\']([^"\']+)["\']', c)
        for s in re.findall(r'srcset=["\']([^"\']+)["\']', c):
            for part in s.split(','):
                clean = part.strip().split(' ')[0]
                if clean:
                    imgs.append(clean)
        for img in imgs:
            if not img.startswith(('http', 'data:')):
                used_images.add(os.path.basename(img.split('?')[0]))

print("Images used in Services 1-6:")
for u in sorted(used_images):
    print("  ", u)

# 2. Check dropbox photos
db_files = [f for f in os.listdir(db_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]
print(f"\nTotal photos in dropbox_photos: {len(db_files)}")

# Also inspect mockup image
mockup_path = r"C:\Users\ekta bansal\.gemini\antigravity\brain\f5f3c267-89c4-44aa-8b83-5fc2de891e69\.user_uploaded\media_1795432010914_cc8da773.jpg"
if os.path.exists(mockup_path):
    m = Image.open(mockup_path)
    print(f"\nMockup size: {m.size}")

# Check existing gbp assets in assets/services
gbp_assets = glob.glob(os.path.join(base_dir, "assets", "services", "*gbp*"))
print("\nExisting gbp assets in assets/services:")
for g in gbp_assets:
    print("  ", os.path.basename(g), os.path.getsize(g))
