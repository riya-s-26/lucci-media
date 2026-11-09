import os
from PIL import Image

p1 = 'C:/Users/riyas/.gemini/antigravity/brain/91a1ccde-d165-4dfe-810e-513091b2e231/.user_uploaded/media_1794227905001_00ef3a0b.png'
p2 = 'C:/Users/riyas/.gemini/antigravity/brain/91a1ccde-d165-4dfe-810e-513091b2e231/.user_uploaded/media_1794227908304_44957956.png'

im1 = Image.open(p1)
im2 = Image.open(p2)

print("Uploaded Ref 1 (Horizontal):", im1.size, im1.mode)
print("Uploaded Ref 2 (Stacked):", im2.size, im2.mode)

# Let's inspect assets in the project:
for f in ['assets/lucci-client-logo-black.png', 'assets/lucci-client-logo-dark.png', 'assets/lucci-mark-dark.png']:
    im = Image.open(f)
    print(f, im.size, im.mode)

