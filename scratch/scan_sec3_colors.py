from PIL import Image

im = Image.open('scratch/sec3_rows.png')
w, h = im.size
print("sec3_rows size:", w, h)
for y in range(0, h, 10):
    c = im.getpixel((10, y))
    print(f"y={y}: color={c}")

