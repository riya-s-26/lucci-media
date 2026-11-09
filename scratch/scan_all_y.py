from PIL import Image

im = Image.open('review/desktop_about.png').convert('RGB')
bg = (253, 253, 252)

# Scan every 20px from top to bottom
for y in range(0, im.height, 20):
    row = [im.getpixel((x, y)) for x in range(im.width)]
    non_bg = sum(1 for p in row if p != bg)
    if non_bg > 50:
        print(f"y={y:4d}: non-bg = {non_bg:4d}")

