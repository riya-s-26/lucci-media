from PIL import Image

for f in ['bot_05.jpg', 'bot_09.jpg', 'top_01.jpg', 'top_08.jpg', 'top_13.jpg']:
    im = Image.open('assets/archive/' + f)
    thumb = im.resize((200, 250))
    thumb.save(f'scratch/thumb_{f}', quality=80)
    print(f"Saved scratch/thumb_{f}")

