import os
from PIL import Image, ImageDraw, ImageFont

# Let's inspect the exact font sizes and vertical positions in Section 03
ref = Image.open(r'C:\Users\riyas\.gemini\antigravity\brain\91a1ccde-d165-4dfe-810e-513091b2e231\.user_uploaded\media_1794049842470_6953d09f.jpg')
w, h = ref.size
print(f"Base mockup size: {w} x {h}")

# In 1x coordinates:
# Section 03 rows area:
# x starts around 300, extends to 650 (margin on right is ~32px, so 682-32 = 650)
# y starts around 662, extends to 800 (height ~138px)
# 4 rows -> ~34.5px per row
# Divider lines at y = 662, 696, 731, 765, 800

