from PIL import Image

# Let's inspect what is in lex-studio-pose.jpg
im = Image.open('assets/lucci/lex-studio-pose.jpg')
print("lex-studio-pose size:", im.size)
# Let's check the colors across a 5x5 grid
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

