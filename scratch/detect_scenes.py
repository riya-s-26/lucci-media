import os
from PIL import Image

db_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\dropbox_photos"

# Let's inspect the files:
# Let's see what each of the top candidates looks like
def inspect_candidate(fname):
    p = os.path.join(db_dir, fname)
    im = Image.open(p)
    w, h = im.size
    print(f"\nCandidate: {fname} ({w}x{h})")
    # Check if there is skin tone (R > 180, G in 120-170, B in 100-150)
    # Check if there is architecture / interior / marble
    sample = im.resize((100, 100)).convert('RGB')
    skin_pixels = 0
    white_bright = 0
    dark_pixels = 0
    for px in sample.getdata():
        r, g, b = px
        if r > 160 and g > 110 and b > 80 and (r - g) > 20 and (r - b) > 30:
            skin_pixels += 1
        if r > 210 and g > 210 and b > 210:
            white_bright += 1
        if r < 50 and g < 50 and b < 50:
            dark_pixels += 1
    print(f"  Skin %: {skin_pixels/100:.1f}%, Bright/White %: {white_bright/100:.1f}%, Dark %: {dark_pixels/100:.1f}%")

for f in ["IMG_0020.JPG", "IMG_0021.JPG", "IMG_4088.JPG", "DSC08037.JPG", "DSC00336.JPG", "DSC02158.JPG", "DSC05862.JPG", "IMG_8364.jpg", "IMG_9983.JPG"]:
    inspect_candidate(f)
