import os
from PIL import Image, ImageDraw, ImageFont

root = 'scratch/dropbox_extracted'
all_imgs = []

for dirpath, dirs, files in os.walk(root):
    for f in sorted(files):
        if f.lower().endswith(('.jpg', '.jpeg', '.png')):
            p = os.path.join(dirpath, f)
            rel = os.path.relpath(p, root)
            all_imgs.append((p, rel))

print(f"Total images found: {len(all_imgs)}")

# Generate contact sheets of 16 images each (4x4)
thumb_w, thumb_h = 240, 240
cols, rows = 4, 4
per_sheet = cols * rows

for sheet_idx in range(0, len(all_imgs), per_sheet):
    batch = all_imgs[sheet_idx:sheet_idx + per_sheet]
    sheet = Image.new('RGB', (cols * thumb_w, rows * thumb_h), (255, 255, 255))
    draw = ImageDraw.Draw(sheet)

    for i, (p, rel) in enumerate(batch):
        r = i // cols
        c = i % cols
        x = c * thumb_w
        y = r * thumb_h

        try:
            im = Image.open(p)
            im.thumbnail((thumb_w - 10, thumb_h - 30))
            # paste centered in cell
            paste_x = x + (thumb_w - im.size[0]) // 2
            paste_y = y + (thumb_h - 30 - im.size[1]) // 2
            sheet.paste(im, (paste_x, paste_y))
            # draw label
            short_name = os.path.basename(rel)[:26]
            draw.text((x + 5, y + thumb_h - 22), short_name, fill=(0, 0, 0))
        except Exception as e:
            draw.text((x + 5, y + 100), f"Error: {e}", fill=(255, 0, 0))

    sheet_path = f"scratch/contact_sheet_{sheet_idx // per_sheet + 1}.png"
    sheet.save(sheet_path)
    print(f"Saved {sheet_path} with {len(batch)} images.")
