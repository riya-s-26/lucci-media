import os
from PIL import Image

db_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\dropbox_photos"

# Let's inspect the scenes of IMG_0020.JPG and DSC08037.JPG
# What do they portray? Let's analyze regions:
def describe_features(fname):
    p = os.path.join(db_dir, fname)
    im = Image.open(p)
    w, h = im.size
    print(f"\n--- {fname} ({w}x{h}) ---")
    # let's sample 4 corners and center
    print("TL:", im.getpixel((w*0.1, h*0.1)))
    print("TR:", im.getpixel((w*0.9, h*0.1)))
    print("Center:", im.getpixel((w*0.5, h*0.5)))
    print("BL:", im.getpixel((w*0.1, h*0.9)))
    print("BR:", im.getpixel((w*0.9, h*0.9)))

describe_features("IMG_0020.JPG")
describe_features("IMG_0021.JPG")
describe_features("DSC08037.JPG")
describe_features("IMG_9983.JPG")
describe_features("IMG_4088.JPG")
