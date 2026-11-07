from PIL import Image

# Let's inspect mockup_sec3.png and mockup_hero_img.png
im3 = Image.open('scratch/mockup_sec3.png')
print("mockup_sec3 size:", im3.size)

im_hero = Image.open('scratch/mockup_hero_img.png')
print("mockup_hero size:", im_hero.size)

