import os
from PIL import Image

f1 = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\assets\services\google-business-profile-preview.jpg"
f2 = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\assets\services\gbp-hero-main.webp"
f3 = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\assets\services\gbp-who-for.webp"

for f in [f1, f2, f3]:
    if os.path.exists(f):
        im = Image.open(f)
        print(os.path.basename(f), im.size, im.mode)
        # save a 200x200 thumb in scratch to inspect
        im.thumbnail((200, 200))
        im.convert('RGB').save(os.path.join(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch", "thumb_" + os.path.basename(f) + ".jpg"))
