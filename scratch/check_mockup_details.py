from PIL import Image

p = r'C:\Users\riyas\.gemini\antigravity\brain\91a1ccde-d165-4dfe-810e-513091b2e231\.user_uploaded\media_1794049842470_6953d09f.jpg'
im = Image.open(p)
w, h = im.size
print("Mockup size:", w, h)

# Crop Section 03: around y=0.65*h to 0.80*h
sec3 = im.crop((0, int(0.65*h), w, int(0.80*h)))
sec3.save('scratch/mockup_sec3.png')
print("Saved scratch/mockup_sec3.png")

# Also let's inspect the hero image area: y=0.06*h to 0.28*h, x=0.4*w to w
hero_img = im.crop((int(0.4*w), int(0.05*h), w, int(0.28*h)))
hero_img.save('scratch/mockup_hero_img.png')
print("Saved scratch/mockup_hero_img.png")

