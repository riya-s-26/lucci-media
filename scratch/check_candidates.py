import os
from PIL import Image

db_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\dropbox_photos"

# Let's inspect some of these images by resizing to 200x200 and checking colors/luminance
candidates = [
    "IMG_0020.JPG", "IMG_0021.JPG", "IMG_4088.JPG", "IMG_9960.JPG", 
    "IMG_9969.JPG", "IMG_9983.JPG", "DSC00336.JPG", "DSC02158.JPG", 
    "DSC03284.JPG", "DSC05857.JPG", "DSC05862.JPG", "DSC08037.JPG", 
    "IMG_0217 (1).JPG", "IMG_9808.JPG", "IMG_9979.JPG", "Tezza-3818.jpg"
]

print("Candidate image aspect ratios & details:")
for c in candidates:
    p = os.path.join(db_dir, c)
    im = Image.open(p)
    print(f"{c:18}: {im.size} AR: {im.width/im.height:.2f}")
