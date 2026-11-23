import os
from PIL import Image

db_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\dropbox_photos"
files = [os.path.join(db_dir, f) for f in os.listdir(db_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

c1_hero = Image.open(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\concept1_hero_crop.jpg").convert('RGB')
c1_who = Image.open(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\concept1_who_crop.jpg").convert('RGB')

# Let's check color histograms or thumbnail differences to find any match in dropbox
c1_hero_thumb = c1_hero.resize((50, 50))
c1_who_thumb = c1_who.resize((50, 50))

best_hero_match = (None, 999999)
best_who_match = (None, 999999)

for f in files:
    try:
        im = Image.open(f).convert('RGB')
        t = im.resize((50, 50))
        # calc diff
        d_h = sum(abs(p1 - p2) for p1, p2 in zip(t.tobytes(), c1_hero_thumb.tobytes())) / (50*50*3)
        d_w = sum(abs(p1 - p2) for p1, p2 in zip(t.tobytes(), c1_who_thumb.tobytes())) / (50*50*3)
        if d_h < best_hero_match[1]:
            best_hero_match = (os.path.basename(f), d_h)
        if d_w < best_who_match[1]:
            best_who_match = (os.path.basename(f), d_w)
    except Exception as e:
        pass

print("Best hero match in dropbox:", best_hero_match)
print("Best who match in dropbox:", best_who_match)
