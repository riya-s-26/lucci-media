import os
from PIL import Image

sample_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\horizontal_samples"

# Let's inspect each image's features:
# We can check colors across top, middle, bottom
for fname in os.listdir(sample_dir):
    im = Image.open(os.path.join(sample_dir, fname)).convert('RGB')
    w, h = im.size
    # top 30%
    top = im.crop((0, 0, w, int(h*0.3))).resize((1, 1)).getpixel((0, 0))
    # mid 40%
    mid = im.crop((0, int(h*0.3), w, int(h*0.7))).resize((1, 1)).getpixel((0, 0))
    # bot 30%
    bot = im.crop((0, int(h*0.7), w, h)).resize((1, 1)).getpixel((0, 0))
    print(f"{fname:30} | Top: {top} | Mid: {mid} | Bot: {bot}")
