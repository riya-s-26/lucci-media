from PIL import Image

for f in ['product-content.webp', 'brown-sugar-skin.webp', 'behind-the-lens.webp', 'on-set.webp', 'studio-story.webp']:
    im = Image.open('assets/' + f)
    w, h = im.size
    # let's sample colors in a 3x3 grid
    grid = []
    for y in range(3):
        for x in range(3):
            box = (x*w//3, y*h//3, (x+1)*w//3, (y+1)*h//3)
            c = im.crop(box).convert('RGB').resize((1, 1)).getpixel((0,0))
            lum = int(0.299*c[0] + 0.587*c[1] + 0.114*c[2])
            grid.append(lum)
    print(f"{f:22}: {grid}")

