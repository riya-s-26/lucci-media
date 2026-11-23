import os
from PIL import Image

# Let's inspect the files in dropbox_photos
db_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\dropbox_photos"

# Let's check:
# In previous sessions, what images were identified in dropbox_photos?
# Let's search previous python scripts in lucci-media/scratch for references to dropbox filenames
import glob
py_files = glob.glob(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\*.py")
for pf in py_files:
    with open(pf, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
    for fname in ["DSC", "IMG_", "Tezza"]:
        if fname in text:
            for line in text.split('\n'):
                if any(x in line for x in ["DSC0", "IMG_", "Tezza-"]) and any(x in line for x in ["#", "print", "hero", "who", "match", "treatment", "clinic", "interior"]):
                    print(f"{os.path.basename(pf)}: {line.strip()[:100]}")
