# Let's inspect the visual subjects of these images
import os
from PIL import Image

def analyze_subject(p):
    im = Image.open(p)
    w, h = im.size
    # let's sample colors in a 3x3 grid
    grid = []
    for y in range(3):
        for x in range(3):
            box = (x*w//3, y*h//3, (x+1)*w//3, (y+1)*h//3)
            c = im.crop(box).convert('RGB').resize((1, 1)).getpixel((0,0))
            lum = int(0.299*c[0] + 0.587*c[1] + 0.114*c[2])
            grid.append(lum)
    return grid

for f in ['bot_04.jpg', 'bot_05.jpg', 'bot_06.jpg', 'bot_07.jpg', 'bot_09.jpg', 'bot_10.jpg', 'bot_12.jpg', 'bot_13.jpg', 'top_01.jpg', 'top_06.jpg', 'top_08.jpg', 'top_13.jpg']:
    p = os.path.join('assets/archive', f)
    g = analyze_subject(p)
    print(f"{f:12}: {g}")

