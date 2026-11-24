import os
from PIL import Image

def smart_crop(im, target_w, target_h, center_x_pct=0.5, center_y_pct=0.5):
    src_w, src_h = im.size
    target_ratio = target_w / target_h
    src_ratio = src_w / src_h

    if src_ratio > target_ratio:
        new_w = int(src_h * target_ratio)
        new_h = src_h
        ideal_x = int(src_w * center_x_pct)
        x1 = max(0, min(src_w - new_w, ideal_x - new_w // 2))
        y1 = 0
    else:
        new_w = src_w
        new_h = int(src_w / target_ratio)
        ideal_y = int(src_h * center_y_pct)
        x1 = 0
        y1 = max(0, min(src_h - new_h, ideal_y - new_h // 2))

    cropped = im.crop((x1, y1, x1 + new_w, y1 + new_h))
    return cropped

tasks = [
    # 1. Campaign Shoots Hero
    ('campaign-shoots-hero', 'scratch/dropbox_extracted/DSC08037.JPG', 1080, 760, 0.5, 0.45),
    # 2. Campaign Shoots Details
    ('campaign-shoots-details', 'scratch/dropbox_extracted/IMG_8567.jpg', 760, 600, 0.5, 0.4),
    # 3. Campaign Shoots Proof Banner
    ('campaign-shoots-silk', 'scratch/dropbox_extracted/Work/IMG_5893.JPG', 1420, 336, 0.5, 0.52),
    # 4. Brand Identity Hero
    ('brand-identity-hero', 'scratch/dropbox_extracted/IMG_9969.JPG', 1080, 820, 0.5, 0.5),
    # 5. Brand Identity Who
    ('brand-identity-who', 'scratch/dropbox_extracted/DSC08107.JPG', 960, 880, 0.5, 0.65),
    # 6. Website Design Hero
    ('website-design-hero', 'scratch/dropbox_extracted/Tezza-3818.jpg', 1080, 760, 0.52, 0.48),
    # 7. Website Design Who
    ('website-design-who', 'scratch/dropbox_extracted/Templates/LANDSCAPE TEMPLATES - 7.JPG', 960, 720, 0.5, 0.5),
]

dest_dir = 'assets/services'
os.makedirs(dest_dir, exist_ok=True)

for name, src_path, w2x, h2x, cx, cy in tasks:
    im = Image.open(src_path)
    cropped = smart_crop(im, w2x, h2x, cx, cy)

    # 2x High-DPI Retina image
    path_2x = os.path.join(dest_dir, f'{name}@2x.jpg')
    im_2x = cropped.resize((w2x, h2x), Image.Resampling.LANCZOS)
    im_2x.convert('RGB').save(path_2x, quality=94, optimize=True)

    # 1x Standard display image
    w1x = w2x // 2
    h1x = h2x // 2
    path_1x = os.path.join(dest_dir, f'{name}.jpg')
    im_1x = cropped.resize((w1x, h1x), Image.Resampling.LANCZOS)
    im_1x.convert('RGB').save(path_1x, quality=94, optimize=True)

    print(f"Generated: {name}@2x.jpg ({w2x}x{h2x}) & {name}.jpg ({w1x}x{h1x})")

print("All production assets deployed successfully.")
