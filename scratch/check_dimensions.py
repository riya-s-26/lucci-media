import os
from PIL import Image

db_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\dropbox_photos"

# Let's inspect some candidate images:
# Let's write a python script to print brightness, color variance, edge complexity
for name in ["IMG_0020.JPG", "IMG_0021.JPG", "IMG_8364.jpg", "DSC00336.JPG", "DSC08037.JPG", "IMG_4088.JPG", "IMG_9983.JPG"]:
    im = Image.open(os.path.join(db_dir, name))
    print(f"Name: {name}, Dimensions: {im.size}, Aspect Ratio: {im.width/im.height:.2f}")
