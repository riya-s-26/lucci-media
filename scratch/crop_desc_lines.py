from PIL import Image

for i in range(1, 5):
    im = Image.open(f'scratch/row_{i}.png')
    w, h = im.size
    # let's look at the description region: x = 200..w
    desc_crop = im.crop((200, 0, w, h))
    desc_crop.save(f'scratch/desc_crop_{i}.png')
    print(f"Saved desc_crop_{i}.png")

