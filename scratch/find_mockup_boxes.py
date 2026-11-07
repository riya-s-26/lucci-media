from PIL import Image

ref_path = r'C:\Users\riyas\.gemini\antigravity\brain\91a1ccde-d165-4dfe-810e-513091b2e231\.user_uploaded\media_1794049842470_6953d09f.jpg'
im = Image.open(ref_path)
w, h = im.size

# Let's inspect the hero image region
# In Reference Image 1:
# The header is at the top y=0..45
# Hero text is on the left x=38..300, y=70..250
# Hero image is on the right x=280..682, y=50..280
# Let's find the exact bounding box of the hero image
# We can find where the image starts on the right
hero_box_crop = im.crop((280, 45, 682, 285))
hero_box_crop.save('scratch/ref_hero_region.png')
print("Saved scratch/ref_hero_region.png size:", hero_box_crop.size)

# Also let's inspect Section 03 region:
sec3_box_crop = im.crop((0, 650, 682, 800))
sec3_box_crop.save('scratch/ref_sec3_region.png')
print("Saved scratch/ref_sec3_region.png size:", sec3_box_crop.size)

