import os
from PIL import Image

thumbs_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\db_thumbs"
srv_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\assets\services"
db_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\dropbox_photos"

# Load thumb mapping
files = [f for f in os.listdir(db_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]
# in classify_dropbox.py, thumb_{i}.jpg corresponded to files[i]

def match_target(target_path, name):
    target = Image.open(target_path).convert('RGB').resize((50, 50))
    best_file = None
    best_diff = 999999
    
    for i, fname in enumerate(files):
        t_path = os.path.join(thumbs_dir, f"thumb_{i}.jpg")
        if os.path.exists(t_path):
            t = Image.open(t_path).convert('RGB').resize((50, 50))
            d = sum(abs(a - b) for a, b in zip(t.tobytes(), target.tobytes())) / (50 * 50 * 3)
            if d < best_diff:
                best_diff = d
                best_file = fname
    print(f"{name:35} -> Best match: {best_file} (diff: {best_diff:.2f})")

match_target(os.path.join(srv_dir, "google-business-profile-preview.jpg"), "google-business-profile-preview.jpg")
match_target(os.path.join(srv_dir, "gbp-hero-main.webp"), "gbp-hero-main.webp")
match_target(os.path.join(srv_dir, "gbp-who-for.webp"), "gbp-who-for.webp")
match_target(os.path.join(srv_dir, "gbp-cta.webp"), "gbp-cta.webp")
