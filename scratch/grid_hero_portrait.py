from PIL import Image

im = Image.open('assets/hero-lex-portrait.jpg')
print("hero-lex-portrait size:", im.size)
w, h = im.size
rgb = im.convert('RGB')
for y in range(0, 5):
    row = []
    for x in range(0, 5):
        box = (x * w // 5, y * h // 5, (x+1) * w // 5, (y+1) * h // 5)
        c = rgb.crop(box).resize((1, 1)).getpixel((0,0))
        lum = int(0.299*c[0] + 0.587*c[1] + 0.114*c[2])
        row.append(f"{lum:3}")
    print(" ".join(row))

