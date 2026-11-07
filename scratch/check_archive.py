from PIL import Image

# Check bot_04.jpg
im_bot4 = Image.open('assets/archive/bot_04.jpg')
print('bot_04 size:', im_bot4.size)
im_bot4.thumbnail((400, 400))
im_bot4.save('scratch/thumb_bot_04.jpg')

# Check what images exist in assets/archive
for i in range(1, 14):
    for prefix in ['top', 'bot']:
        path = f'assets/archive/{prefix}_{i:02d}.jpg'
        try:
            im = Image.open(path)
            # save small thumb
            im.thumbnail((150, 150))
            im.save(f'scratch/archive_{prefix}_{i:02d}.jpg')
        except:
            pass

print('Archive thumbs generated.')

