import os
import re
from PIL import Image

# Check scratch_luccimedia.html for all logos
if os.path.exists('scratch_luccimedia.html'):
    with open('scratch_luccimedia.html', 'r', encoding='utf-8', errors='ignore') as f:
        txt = f.read()
    logos = re.findall(r'//static\.showit\.co/[^\s"\'\)]+?branding[^\s"\'\)]*', txt)
    print("Branding images in Showit HTML:", set(logos))
    all_logos = re.findall(r'//static\.showit\.co/[^\s"\'\)]+?logo[^\s"\'\)]*', txt)
    print("Logo images in Showit HTML:", set(all_logos))

# Let's inspect lucci-client-logo-black.png vs lucci-mark-dark.png
im1 = Image.open('assets/lucci-client-logo-black.png')
im2 = Image.open('assets/lucci-mark-dark.png')

print("lucci-client-logo-black size:", im1.size)
print("lucci-mark-dark size:", im2.size)

# Let's check bbox of non-transparent pixels
print("im1 bbox:", im1.getbbox())
print("im2 bbox:", im2.getbbox())

