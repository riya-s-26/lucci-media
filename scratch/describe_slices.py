import os
from PIL import Image

db_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\dropbox_photos"

# Let's inspect the files in detail
# We can look at the images by saving 10 slices of each or checking what objects are in them
def describe_slices(fname):
    p = os.path.join(db_dir, fname)
    im = Image.open(p)
    w, h = im.size
    print(f"\n=== {fname} ({w}x{h}) ===")
    # Print color summary for top half and bottom half
    top_avg = im.crop((0, 0, w, h//2)).resize((1, 1)).getpixel((0, 0))
    bot_avg = im.crop((0, h//2, w, h)).resize((1, 1)).getpixel((0, 0))
    left_avg = im.crop((0, 0, w//2, h)).resize((1, 1)).getpixel((0, 0))
    right_avg = im.crop((w//2, 0, w, h)).resize((1, 1)).getpixel((0, 0))
    print(f"  Top: {top_avg}, Bottom: {bot_avg}")
    print(f"  Left: {left_avg}, Right: {right_avg}")

describe_slices("IMG_0020.JPG")
describe_slices("IMG_0021.JPG")
describe_slices("DSC08037.JPG")
describe_slices("IMG_4088.JPG")
describe_slices("IMG_9983.JPG")
describe_slices("DSC00336.JPG")
