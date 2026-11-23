import os
from PIL import Image

db_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\dropbox_photos"

# Let's inspect the files in dropbox_photos
# We can check what kinds of scenes they are:
# For example, does IMG_0020 show an interior, a salon, a med spa?
# Does DSC00336 show a treatment room?
# Does IMG_4088 show an injector or reception?

def check_image(name):
    im = Image.open(os.path.join(db_dir, name))
    # Let's check brightness distribution
    gray = im.convert('L')
    hist = gray.histogram()
    avg_lum = sum(i * count for i, count in enumerate(hist)) / sum(hist)
    # Check color saturation
    rgb = im.convert('RGB')
    # sample 100 pixels
    diffs = []
    for x in range(0, im.width, im.width // 10):
        for y in range(0, im.height, im.height // 10):
            r, g, b = rgb.getpixel((x, y))
            diffs.append(max(r, g, b) - min(r, g, b))
    avg_sat = sum(diffs) / len(diffs)
    print(f"{name:15}: size={im.size}, lum={avg_lum:.1f}, sat={avg_sat:.1f}")

for f in ["IMG_0020.JPG", "IMG_0021.JPG", "IMG_8364.jpg", "IMG_4088.JPG", "DSC00336.JPG", "DSC08037.JPG", "IMG_9960.JPG", "IMG_9983.JPG", "DSC05857.JPG", "DSC05862.JPG"]:
    check_image(f)
