from PIL import Image

for i in range(1, 5):
    im = Image.open(f'scratch/row_{i}.png')
    w, h = im.size
    # let's find the background color (most common color or top-left)
    bg = im.getpixel((5, 5))
    # let's find the y position of the divider line (if any)
    print(f"Row {i} ({w}x{h}): bg={bg}")

