import os
import glob
from PIL import Image

def find_images():
    print("Searching dropbox_photos...")
    db_files = glob.glob(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\dropbox_photos\**\*.*", recursive=True)
    print(f"Total dropbox files found: {len(db_files)}")
    
    # Check for laptop or website or desk images
    keywords = ["laptop", "desk", "computer", "screen", "macbook", "phone", "iphone", "book", "candle"]
    matches = []
    for f in db_files:
        basename = os.path.basename(f).lower()
        if any(k in basename for k in keywords):
            matches.append(f)
    print(f"Keyword matches in dropbox: {len(matches)}")
    for m in matches[:20]:
        print(" ", os.path.basename(m))

    # Also check assets/services
    print("\nChecking assets/services...")
    srv_files = glob.glob(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\assets\services\*.*")
    for f in srv_files:
        b = os.path.basename(f)
        if "web" in b.lower():
            print(" ", b, os.path.getsize(f), Image.open(f).size if f.lower().endswith(('.jpg','.png','.webp')) else "")

if __name__ == "__main__":
    find_images()
