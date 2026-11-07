from PIL import Image

for i in range(1, 5):
    im = Image.open(f'scratch/desc_crop_{i}.png').convert('L')
    w, h = im.size
    # count dark pixels in each horizontal scanline y
    bands = []
    in_band = False
    for y in range(h):
        dark_in_y = sum(1 for x in range(w) if im.getpixel((x, y)) < 200)
        if dark_in_y > 10 and not in_band:
            in_band = True
            bands.append(y)
        elif dark_in_y <= 10 and in_band:
            in_band = False
    print(f"Desc {i}: {len(bands)} text lines detected at y={bands}")

