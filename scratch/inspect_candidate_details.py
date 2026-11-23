import os
from PIL import Image

cand_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\gbp_candidates"

for f in sorted(os.listdir(cand_dir)):
    im = Image.open(os.path.join(cand_dir, f))
    # Sample a grid of 5x5 pixels
    colors = []
    w, h = im.size
    for x in range(w//6, w, w//6):
        for y in range(h//6, h, h//6):
            colors.append(im.getpixel((x, y)))
    # calculate average color and variance
    avg_r = sum(c[0] for c in colors)//len(colors)
    avg_g = sum(c[1] for c in colors)//len(colors)
    avg_b = sum(c[2] for c in colors)//len(colors)
    print(f"{f:25} | Avg: ({avg_r},{avg_g},{avg_b}) | Size: {im.size}")
