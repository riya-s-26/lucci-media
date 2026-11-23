import os
from PIL import Image, ImageEnhance

db_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\dropbox_photos"
out_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\assets\services"

def process_image(src_name, target_w, target_h, base_name):
    src_path = os.path.join(db_dir, src_name)
    im = Image.open(src_path).convert('RGB')
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
        
    # Generate @2x
    w2x, h2x = target_w * 2, target_h * 2
    im_2x = crop.resize((w2x, h2x), Image.Resampling.LANCZOS)
    enhancer = ImageEnhance.Sharpness(im_2x)
    im_2x = enhancer.enhance(1.2)
    
    # Generate 1x
    im_1x = im_2x.resize((target_w, target_h), Image.Resampling.LANCZOS)
    
    path_1x = os.path.join(out_dir, f"{base_name}.jpg")
    path_2x = os.path.join(out_dir, f"{base_name}@2x.jpg")
    
    im_1x.save(path_1x, "JPEG", quality=92, optimize=True)
    im_2x.save(path_2x, "JPEG", quality=90, optimize=True)
    
    print(f"Generated {path_1x}: {im_1x.size} ({os.path.getsize(path_1x)} bytes)")
    print(f"Generated {path_2x}: {im_2x.size} ({os.path.getsize(path_2x)} bytes)")

# 1. Hero Image: 540x380 (1080x760 @2x)
process_image("DSC08037.JPG", 540, 380, "google-business-profile-hero")

# 2. Who It's For Image: 480x360 (960x720 @2x)
process_image("IMG_0020.JPG", 480, 360, "google-business-profile-who")

print("All GBP image assets generated successfully!")
