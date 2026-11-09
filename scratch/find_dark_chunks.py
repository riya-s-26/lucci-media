from PIL import Image

im = Image.open('review/desktop_about.png').convert('RGB')
# Let's count dark pixels (< 50) in 50px chunks along y
for y in range(0, im.height, 100):
    box = im.crop((0, y, im.width, min(im.height, y + 100)))
    dark_count = sum(1 for p in box.getdata() if p[0] < 50 and p[1] < 50 and p[2] < 50)
    if dark_count > 100:
        print(f"y={y:4d} to {y+100:4d}: dark pixels = {dark_count:6d}")

