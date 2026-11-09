import os
from PIL import Image

for f in sorted(os.listdir('scratch')):
    if f.startswith('mobile_slice_'):
        p = os.path.join('scratch', f)
        im = Image.open(p)
        print(f, im.size)

