import os
from PIL import Image

def analyze_image_subjects():
    # Let's inspect gbp-hero-main, gbp-who-for, IMG_0020, IMG_8364, IMG_4088, DSC08037
    # Let's see what each image looks like
    db_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\dropbox_photos"
    srv_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\assets\services"
    
    # We can check colors, contrast, brightness, skin tones, etc.
    for fname in ["IMG_0020.JPG", "IMG_0021.JPG", "IMG_8364.jpg", "IMG_4088.JPG", "DSC08037.JPG", "DSC00336.JPG"]:
        p = os.path.join(db_dir, fname)
        im = Image.open(p)
        print(f"File {fname}: {im.size}")

if __name__ == "__main__":
    analyze_image_subjects()
