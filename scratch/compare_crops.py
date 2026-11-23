import os
from PIL import Image

# Let's inspect concept1_hero_crop and compare with website-design-preview.jpg
c1_hero = Image.open(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\concept1_hero_crop.jpg")
c1_who = Image.open(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\concept1_who_crop.jpg")
prev = Image.open(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\assets\services\website-design-preview.jpg")

print("C1 Hero size:", c1_hero.size)
print("C1 Who size:", c1_who.size)
print("Preview size:", prev.size)

# Let's check if the preview is the same image or something else
# Let's resize preview to c1_hero size and compare
prev_resized = prev.resize(c1_hero.size)
# calculate difference
diff = 0
for x in range(c1_hero.width):
    for y in range(c1_hero.height):
        p1 = c1_hero.getpixel((x, y))
        p2 = prev_resized.getpixel((x, y))
        diff += sum(abs(a - b) for a, b in zip(p1, p2))
avg_diff = diff / (c1_hero.width * c1_hero.height * 3)
print("Average difference between C1 hero crop and preview.jpg:", avg_diff)
