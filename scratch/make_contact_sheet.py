import os
from PIL import Image

db_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\dropbox_photos"
candidates = [
    "IMG_0020.JPG", "IMG_0021.JPG", "IMG_4088.JPG", "IMG_9960.JPG", 
    "IMG_9969.JPG", "IMG_9983.JPG", "DSC00336.JPG", "DSC02158.JPG", 
    "DSC03284.JPG", "DSC05857.JPG", "DSC05862.JPG", "DSC08037.JPG", 
    "IMG_0217 (1).JPG", "IMG_9808.JPG", "IMG_9979.JPG", "Tezza-3818.jpg",
    "DSC08107.JPG", "DSC08166.JPG", "IMG_4072.JPG", "IMG_4075.JPG"
]

# Let's save a mosaic or contact sheet so we can understand the scenes
contact = Image.new('RGB', (1600, 1000), (255, 255, 255))
col, row = 0, 0
cw, ch = 320, 200

for c in candidates:
    p = os.path.join(db_dir, c)
    im = Image.open(p)
    im.thumbnail((cw, ch))
    # paste onto contact sheet
    contact.paste(im, (col * cw, row * ch))
    col += 1
    if col >= 5:
        col = 0
        row += 1

contact_path = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\contact_sheet.jpg"
contact.save(contact_path, quality=85)
print("Saved contact sheet to:", contact_path)
