import os
from PIL import Image

db_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\dropbox_photos"
srv_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\assets\services"

db_files = [f for f in os.listdir(db_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]

def find_match(target_path, name):
    target = Image.open(target_path).convert('RGB')
    target_thumb = target.resize((60, 60))
    best_file = None
    best_diff = 999999
    
    for f in db_files:
        p = os.path.join(db_dir, f)
        try:
            im = Image.open(p).convert('RGB')
            # Check aspect ratio compatibility
            thumb = im.resize((60, 60))
            d = sum(abs(a - b) for a, b in zip(thumb.tobytes(), target_thumb.tobytes())) / (60 * 60 * 3)
            if d < best_diff:
                best_diff = d
                best_file = f
        except Exception:
            pass
    print(f"Match for {name}: {best_file} (diff: {best_diff:.2f})")

find_match(os.path.join(srv_dir, "google-business-profile-preview.jpg"), "google-business-profile-preview.jpg")
find_match(os.path.join(srv_dir, "gbp-hero-main.webp"), "gbp-hero-main.webp")
find_match(os.path.join(srv_dir, "gbp-who-for.webp"), "gbp-who-for.webp")
find_match(os.path.join(srv_dir, "gbp-cta.webp"), "gbp-cta.webp")
