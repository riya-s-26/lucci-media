import os
from PIL import Image, ImageEnhance

db_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\dropbox_photos"
out_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch"

# Let's crop DSC08037.JPG for hero: 540x380 (1.42 AR)
im_hero = Image.open(os.path.join(db_dir, "DSC08037.JPG"))
# w=7008, h=4672 (1.50 AR)
target_h = int(im_hero.width / (540 / 380))
top = (im_hero.height - target_h) // 2
crop_hero = im_hero.crop((0, max(0, top), im_hero.width, min(im_hero.height, top + target_h)))
crop_hero_540 = crop_hero.resize((540, 380), Image.Resampling.LANCZOS)
crop_hero_540.save(os.path.join(out_dir, "test_gbp_hero.jpg"), quality=90)

# Let's crop IMG_0020.JPG for who-it's-for: 480x360 (1.33 AR)
im_who = Image.open(os.path.join(db_dir, "IMG_0020.JPG"))
# w=5472, h=3648 (1.50 AR)
target_w = int(im_who.height * (480 / 360))
left = (im_who.width - target_w) // 2
crop_who = im_who.crop((left, 0, left + target_w, im_who.height))
crop_who_480 = crop_who.resize((480, 360), Image.Resampling.LANCZOS)
crop_who_480.save(os.path.join(out_dir, "test_gbp_who.jpg"), quality=90)

print("Generated test_gbp_hero.jpg and test_gbp_who.jpg successfully!")
