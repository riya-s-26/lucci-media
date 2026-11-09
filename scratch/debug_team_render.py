from PIL import Image

im = Image.open('scratch/full_team_region.png')
# let's find the bounding box of each card
# Card 1, 2, 3, 4
print("Image size:", im.size)
# Let's inspect where pixels differ from background #FDFDFC
bg = (253, 253, 252)
for y in range(0, im.height, 50):
    row_diff = sum(1 for x in range(im.width) if im.getpixel((x, y)) != bg)
    if row_diff > 0:
        # find min x and max x
        xs = [x for x in range(im.width) if im.getpixel((x, y)) != bg]
        print(f"y={y:4d}: xs from {min(xs)} to {max(xs)}, count = {len(xs)}")

