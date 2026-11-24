import os
from PIL import Image

def smart_crop(im, target_w, target_h, center_x_pct=0.5, center_y_pct=0.5):
    """Crops image to exact aspect ratio around specified center point."""
    src_w, src_h = im.size
    target_ratio = target_w / target_h
    src_ratio = src_w / src_h

    if src_ratio > target_ratio:
        # Source is wider than target: crop width
        new_w = int(src_h * target_ratio)
        new_h = src_h
        # Calculate x crop bounds around center_x_pct
        ideal_x = int(src_w * center_x_pct)
        x1 = max(0, min(src_w - new_w, ideal_x - new_w // 2))
        y1 = 0
    else:
        # Source is taller than target: crop height
        new_w = src_w
        new_h = int(src_w / target_ratio)
        # Calculate y crop bounds around center_y_pct
        ideal_y = int(src_h * center_y_pct)
        x1 = 0
        y1 = max(0, min(src_h - new_h, ideal_y - new_h // 2))

    cropped = im.crop((x1, y1, x1 + new_w, y1 + new_h))
    return cropped

tasks = [
    # 1. Campaign Shoots Hero: DSC08037.JPG -> 1080x760 (540x380)
    ('campaign-shoots-hero', 'scratch/dropbox_extracted/DSC08037.JPG', 1080, 760, 0.5, 0.45),
    # 2. Campaign Shoots Details: IMG_8567.jpg -> 760x600 (380x300)
    ('campaign-shoots-details', 'scratch/dropbox_extracted/IMG_8567.jpg', 760, 600, 0.5, 0.4),
    # 3. Campaign Shoots Proof: Work/IMG_5893.JPG -> 1420x336 (710x168)
    ('campaign-shoots-silk', 'scratch/dropbox_extracted/Work/IMG_5893.JPG', 1420, 336, 0.5, 0.42),
    # 4. Brand Identity Hero: IMG_9969.JPG -> 1080x820 (540x410)
    ('brand-identity-hero', 'scratch/dropbox_extracted/IMG_9969.JPG', 1080, 820, 0.5, 0.5),
    # 5. Brand Identity Who: DSC08107.JPG -> 960x880 (480x440)
    ('brand-identity-who', 'scratch/dropbox_extracted/DSC08107.JPG', 960, 880, 0.5, 0.65),
    # 6. Website Design Hero: Tezza-3818.jpg -> 1080x760 (540x380)
    ('website-design-hero', 'scratch/dropbox_extracted/Tezza-3818.jpg', 1080, 760, 0.52, 0.48),
    # 7. Website Design Who: Templates/LANDSCAPE TEMPLATES - 7.JPG -> 960x720 (480x360)
    ('website-design-who', 'scratch/dropbox_extracted/Templates/LANDSCAPE TEMPLATES - 7.JPG', 960, 720, 0.5, 0.5),
]

os.makedirs('scratch/cropped_preview', exist_ok=True)
for name, path, w2x, h2x, cx, cy in tasks:
    im = Image.open(path)
    cropped = smart_crop(im, w2x, h2x, cx, cy)
    # 2x image
    im_2x = cropped.resize((w2x, h2x), Image.Resampling.LANCZOS)
    im_2x.convert('RGB').save(f'scratch/cropped_preview/{name}@2x.jpg', quality=92)
    # 1x image
    w1x = w2x // 2
    h1x = h2x // 2
    im_1x = cropped.resize((w1x, h1x), Image.Resampling.LANCZOS)
    im_1x.convert('RGB').save(f'scratch/cropped_preview/{name}.jpg', quality=92)
    print(f"Generated {name}: 2x ({w2x}x{h2x}) and 1x ({w1x}x{h1x}) from {path}")
