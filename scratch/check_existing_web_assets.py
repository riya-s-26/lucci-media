import os
from PIL import Image

srv_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\assets\services"
scratch_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch"

files_to_check = [
    "website-design-preview.jpg",
    "website-design-who-for.webp",
    "website-design-hero-main.webp",
    "website-design-hero-sub.webp",
    "website-design-cta.webp"
]

for f in files_to_check:
    p = os.path.join(srv_dir, f)
    if os.path.exists(p):
        im = Image.open(p)
        print(f, im.size, im.mode)

# Also let's inspect mockup coordinates for left concept
mockup_path = r"C:\Users\ekta bansal\.gemini\antigravity\brain\f5f3c267-89c4-44aa-8b83-5fc2de891e69\.user_uploaded\media_1795430504285_53187fb7.jpg"
m_img = Image.open(mockup_path)
print("Mockup dimensions:", m_img.size) # (1024, 682)

# Concept 1 is left half: x=0 to 512, y=0 to 682
# Let's crop Concept 1 hero and who it's for from the mockup
# In Concept 1, hero image is top right of the left half:
# Left half is 0 to 512.
# Let's crop the exact area of the laptop hero and the phone who it's for.
