import os
from PIL import Image

prev = Image.open(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\assets\services\google-business-profile-preview.jpg")
c2_hero = Image.open(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\gbp_c2_hero.jpg")
c1_hero = Image.open(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\gbp_c1_hero.jpg")

# Compare preview with c2_hero
p_resized = prev.resize(c2_hero.size)
diff_c2 = sum(abs(a - b) for p1, p2 in zip(p_resized.getdata(), c2_hero.getdata()) for a, b in zip(p1, p2)) / (c2_hero.width * c2_hero.height * 3)

# Compare preview with c1_hero
p_resized1 = prev.resize(c1_hero.size)
diff_c1 = sum(abs(a - b) for p1, p2 in zip(p_resized1.getdata(), c1_hero.getdata()) for a, b in zip(p1, p2)) / (c1_hero.width * c1_hero.height * 3)

print("Diff with C2 hero (Storefront blade sign):", diff_c2)
print("Diff with C1 hero (Google maps phone):", diff_c1)
