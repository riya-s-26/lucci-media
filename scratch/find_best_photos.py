import os
from PIL import Image

db_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\dropbox_photos"

# Let's inspect the photos to see what they show:
# Let's examine the aspect ratios and save cropped visual samples
# We have 50 photos. Let's look at the filenames:
# DSC00336.JPG, DSC02158.JPG, DSC03284.JPG, DSC05857.JPG, DSC05862.JPG, DSC08037.JPG
# DSC08067, DSC08107, DSC08166, DSC08171, DSC08232
# IMG_0020, IMG_0021, IMG_0217 (1), IMG_4072, IMG_4075, IMG_4088, IMG_4853, IMG_4854, IMG_4926
# IMG_7091, IMG_7096, IMG_8364, IMG_8365, IMG_8369, IMG_8387, IMG_8390, IMG_9546
# IMG_9808, IMG_9960, IMG_9969, IMG_9979, IMG_9983, IMG_9986
# Tezza-3818, Tezza-6148, Tezza-6504, Tezza-6720

# Let's create an analysis script that inspects their content
print("Analyzing images for beauty business, med spa interior, treatment, storefront...")
for f in os.listdir(db_dir):
    if f.lower().endswith(('.jpg', '.jpeg', '.png')):
        p = os.path.join(db_dir, f)
        im = Image.open(p)
        print(f"{f:35} | AR: {im.width/im.height:.2f} | Size: {im.size}")
