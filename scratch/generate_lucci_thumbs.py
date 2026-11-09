from PIL import Image

lucci_imgs = [
    'assets/lucci/lucci-bts-shoot.jpg',
    'assets/lucci/lucci-bts-studio.jpg',
    'assets/lucci/lucci-bts-table.jpg',
    'assets/lucci/photo_dec_13_2025_2_36_15_pm.jpg',
    'assets/lucci/photo_dec_13_2025_3_46_00_pm.jpg',
    'assets/lucci/lex-camera-onset.jpg',
    'assets/lucci/lex-portrait-main.jpg',
    'assets/lucci/lex-studio-pose.jpg',
]

for p in lucci_imgs:
    im = Image.open(p)
    # create small thumbnail in scratch
    thumb = im.copy()
    thumb.thumbnail((200, 200))
    base = os.path.basename(p)
    thumb_path = f'scratch/inspect_{base}'
    thumb.save(thumb_path)
    print(f"Generated {thumb_path} from {p} (orig: {im.size})")

