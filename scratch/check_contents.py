import os
from PIL import Image

# Let's inspect gbp-hero-main.webp, gbp-who-for.webp, and gbp_c1_hero.jpg
# We can check edge details, color distribution, faces or objects
def check_image_content(img_path, name):
    im = Image.open(img_path)
    print(f"\nImage: {name} ({im.size})")
    # Let's save a clear 400x300 thumbnail with labels
    t = im.copy()
    t.thumbnail((400, 400))
    t.save(rf"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\content_{name}.jpg")
    print(f"Saved content_{name}.jpg")

srv_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\assets\services"
check_image_content(os.path.join(srv_dir, "gbp-hero-main.webp"), "gbp_hero_main")
check_image_content(os.path.join(srv_dir, "gbp-who-for.webp"), "gbp_who_for")
check_image_content(os.path.join(srv_dir, "gbp-cta.webp"), "gbp_cta")
