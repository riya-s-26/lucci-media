import os
from PIL import Image

# Let's inspect content_gbp_hero_main.jpg and content_gbp_who_for.jpg
im1 = Image.open(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\content_gbp_hero_main.jpg")
im2 = Image.open(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\content_gbp_who_for.jpg")

print("im1 size:", im1.size)
print("im2 size:", im2.size)

# Let's check colors in different quarters
def quadrant_colors(im):
    w, h = im.size
    q1 = im.crop((0, 0, w//2, h//2)).resize((1, 1)).getpixel((0, 0))
    q2 = im.crop((w//2, 0, w, h//2)).resize((1, 1)).getpixel((0, 0))
    q3 = im.crop((0, h//2, w//2, h)).resize((1, 1)).getpixel((0, 0))
    q4 = im.crop((w//2, h//2, w, h)).resize((1, 1)).getpixel((0, 0))
    return q1, q2, q3, q4

print("im1 quadrants:", quadrant_colors(im1))
print("im2 quadrants:", quadrant_colors(im2))
