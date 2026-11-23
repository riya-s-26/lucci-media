import os
from PIL import Image

sample_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\horizontal_samples"
files = os.listdir(sample_dir)

# Let's inspect some of them in detail
for f in files:
    im = Image.open(os.path.join(sample_dir, f))
    # Let's get color stats
    stat = im.convert('RGB')
    w, h = stat.size
    print(f"Sample: {f:30} ({w}x{h})")
