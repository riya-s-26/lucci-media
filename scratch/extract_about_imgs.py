from PIL import Image

im = Image.open(r'C:/Users/riyas/.gemini/antigravity/brain/91a1ccde-d165-4dfe-810e-513091b2e231/.user_uploaded/media_1794049842470_6953d09f.jpg')
w, h = im.size
print(f'Full image: {w} x {h}')

# 1. Hero Image:
# In the hero, the image is on the right side.
# Let's find the exact bounding box:
# Top: around y=55 (below header)
# Right: x=w (or near w)
# Bottom: around y=295
# Left: around x=280..290
hero = im.crop((290, 56, 682, 295))
hero.save('assets/about/hero_lex.jpg', quality=95)
print('Saved hero_lex.jpg:', hero.size)

# 2. Section .01: Our Story
# Main treatment room image:
# Left: x=92, Top: y=320, Right: x=318, Bottom: y=498
story_main = im.crop((92, 320, 318, 498))
story_main.save('assets/about/story_treatment_room.jpg', quality=95)
print('Saved story_treatment_room.jpg:', story_main.size)

# Skincare bottles top:
# Left: x=325, Top: y=320, Right: x=397, Bottom: y=408
story_sub1 = im.crop((325, 320, 397, 408))
story_sub1.save('assets/about/story_bottles.jpg', quality=95)
print('Saved story_bottles.jpg:', story_sub1.size)

# Skincare cream texture bottom:
# Left: x=325, Top: y=413, Right: x=397, Bottom: y=498
story_sub2 = im.crop((325, 413, 397, 498))
story_sub2.save('assets/about/story_cream.jpg', quality=95)
print('Saved story_cream.jpg:', story_sub2.size)

# 3. Section .02: How We Think
# Camera monitor shoot:
# Left: x=309, Top: y=520, Right: x=659, Bottom: y=681
think_cam = im.crop((309, 520, 659, 681))
think_cam.save('assets/about/how_we_think_camera.jpg', quality=95)
print('Saved how_we_think_camera.jpg:', think_cam.size)

# 4. Section .04: Meet the Team
# Founder Lex left:
# Left: x=86, Top: y=848, Right: x=275, Bottom: y=987
team_lex = im.crop((86, 848, 275, 987))
team_lex.save('assets/about/team_lex.jpg', quality=95)
print('Saved team_lex.jpg:', team_lex.size)

# Studio chair top right:
# Left: x=525, Top: y=848, Right: x=659, Bottom: y=917
team_studio = im.crop((525, 848, 659, 917))
team_studio.save('assets/about/team_studio_chair.jpg', quality=95)
print('Saved team_studio_chair.jpg:', team_studio.size)

# Team laptop bottom right:
# Left: x=525, Top: y=920, Right: x=659, Bottom: y=987
team_laptop = im.crop((525, 920, 659, 987))
team_laptop.save('assets/about/team_laptop.jpg', quality=95)
print('Saved team_laptop.jpg:', team_laptop.size)

print('All About section images extracted and saved in assets/about/!')

