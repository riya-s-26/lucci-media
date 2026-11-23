import os
from PIL import Image

def describe_img(path, name):
    im = Image.open(path)
    print(f"=== {name} ===")
    print(f"Path: {path}")
    print(f"Dimensions: {im.size}, mode: {im.mode}")
    # Sample 5x5 grid of pixels to get color profile
    colors = []
    for x in [im.width*i//6 for i in range(1, 6)]:
        for y in [im.height*i//6 for i in range(1, 6)]:
            colors.append(im.getpixel((x, y))[:3] if isinstance(im.getpixel((x, y)), tuple) else (im.getpixel((x, y)),)*3)
    avg_r = sum(c[0] for c in colors)//len(colors)
    avg_g = sum(c[1] for c in colors)//len(colors)
    avg_b = sum(c[2] for c in colors)//len(colors)
    print(f"Sampled avg RGB: ({avg_r}, {avg_g}, {avg_b})")

srv_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\assets\services"
for f in ["google-business-profile-preview.jpg", "gbp-hero-main.webp", "gbp-who-for.webp"]:
    p = os.path.join(srv_dir, f)
    if os.path.exists(p):
        describe_img(p, f)

# Also let's inspect the mockup images we cropped
scratch_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch"
describe_img(os.path.join(scratch_dir, "gbp_c1_hero.jpg"), "gbp_c1_hero (Phone with Google Maps)")
describe_img(os.path.join(scratch_dir, "gbp_c1_who.jpg"), "gbp_c1_who (Reception desk with flowers)")
describe_img(os.path.join(scratch_dir, "gbp_c2_hero.jpg"), "gbp_c2_hero (Storefront blade sign)")
describe_img(os.path.join(scratch_dir, "gbp_c2_who.jpg"), "gbp_c2_who (Tablet on desk)")
