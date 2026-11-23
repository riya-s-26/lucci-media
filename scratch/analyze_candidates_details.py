import os
from PIL import Image

db_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\dropbox_photos"

# Let's inspect each candidate specifically
def analyze_candidate(fname):
    p = os.path.join(db_dir, fname)
    im = Image.open(p)
    w, h = im.size
    # let's crop center 30% to see what's in center
    cw, ch = int(w * 0.4), int(h * 0.4)
    crop = im.crop(((w - cw)//2, (h - ch)//2, (w + cw)//2, (h + ch)//2))
    # print basic color distribution
    colors = crop.resize((10, 10)).getdata()
    r = sum(c[0] for c in colors)//100
    g = sum(c[1] for c in colors)//100
    b = sum(c[2] for c in colors)//100
    print(f"{fname:18} | Size: {w}x{h} | Center RGB: ({r},{g},{b})")

for f in ["IMG_0020.JPG", "IMG_0021.JPG", "IMG_4088.JPG", "IMG_9960.JPG", 
          "IMG_9969.JPG", "IMG_9983.JPG", "DSC00336.JPG", "DSC02158.JPG", 
          "DSC03284.JPG", "DSC05857.JPG", "DSC05862.JPG", "DSC08037.JPG", 
          "IMG_0217 (1).JPG", "IMG_9808.JPG", "IMG_9979.JPG", "Tezza-3818.jpg"]:
    analyze_candidate(f)
