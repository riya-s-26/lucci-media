from PIL import Image

# Let's inspect the visual contents of ref_hero_img, ref_story_main, etc.
# Check what bot_04.jpg actually is
im_bot4 = Image.open('assets/archive/bot_04.jpg')
print('bot_04:', im_bot4.size)

# Let's check if bot_04 has the camera monitor:
# In bot_04, let's crop the center and save
w, h = im_bot4.size
im_bot4.crop((w*0.2, h*0.2, w*0.8, h*0.8)).save('scratch/bot_04_center.jpg')
print('Saved bot_04_center.jpg')

