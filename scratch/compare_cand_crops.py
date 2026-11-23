import os
from PIL import Image

db_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\dropbox_photos"
out_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch"

def crop_and_save(src_name, target_w, target_h, out_name):
    im = Image.open(os.path.join(db_dir, src_name))
    ar_target = target_w / target_h
    ar_orig = im.width / im.height
    if ar_orig > ar_target:
        new_w = int(im.height * ar_target)
        left = (im.width - new_w) // 2
        crop = im.crop((left, 0, left + new_w, im.height))
    else:
        new_h = int(im.width / ar_target)
        top = (im.height - new_h) // 2
        crop = im.crop((0, top, im.width, top + new_h))
    res = crop.resize((target_w, target_h), Image.Resampling.LANCZOS)
    p = os.path.join(out_dir, out_name)
    res.save(p, quality=92)
    print(f"Saved {out_name}: {target_w}x{target_h}")

crop_and_save("DSC08037.JPG", 540, 380, "cand_hero_DSC08037.jpg")
crop_and_save("IMG_4088.JPG", 540, 380, "cand_hero_IMG_4088.jpg")
crop_and_save("IMG_0020.JPG", 480, 360, "cand_who_IMG_0020.jpg")
crop_and_save("IMG_0021.JPG", 480, 360, "cand_who_IMG_0021.jpg")
