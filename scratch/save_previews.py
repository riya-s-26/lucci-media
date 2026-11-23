import os
from PIL import Image

db_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\dropbox_photos"

# Let's save small previews to scratch
for name in ["IMG_8364.jpg", "IMG_0020.JPG", "IMG_0021.JPG", "IMG_9979.JPG", "DSC08037.JPG", "DSC00336.JPG", "IMG_4088.JPG"]:
    im = Image.open(os.path.join(db_dir, name))
    im.thumbnail((400, 400))
    im.convert('RGB').save(rf"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\preview_{name}.jpg", quality=80)
    print(f"Saved preview_{name}.jpg ({im.size})")
