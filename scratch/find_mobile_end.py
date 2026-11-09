from PIL import Image

im = Image.open('review/mobile_about.png')
# Let's inspect between y=5200 and y=5600
for y in range(5600, 5000, -10):
    row = [im.getpixel((x, y)) for x in range(im.width)]
    # check if any pixel is non-white and not just background #FDFDFC
    non_bg = sum(1 for p in row if p[0] < 240 or p[1] < 240 or p[2] < 240)
    if non_bg > 5:
        print(f"Content found at y={y} with {non_bg} non-bg pixels")
        break

