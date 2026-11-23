import os
from PIL import Image

# Let's compare gbp_c1_who.jpg with brand-identity-who.jpg and IMG_0020.JPG
c1_who = Image.open(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\gbp_c1_who.jpg")
bi_who = Image.open(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\assets\services\brand-identity-who.jpg")

print("c1_who size:", c1_who.size)
print("bi_who size:", bi_who.size)

# resize bi_who to c1_who
bi_resized = bi_who.resize(c1_who.size)
diff = sum(abs(a - b) for p1, p2 in zip(c1_who.getdata(), bi_resized.getdata()) for a, b in zip(p1, p2)) / (c1_who.width * c1_who.height * 3)
print("Difference between gbp_c1_who and brand-identity-who:", diff)

# Also let's check c2_hero (Storefront blade sign)
c2_hero = Image.open(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\gbp_c2_hero.jpg")
print("c2_hero size:", c2_hero.size)
