from PIL import Image

for i in [3000, 3600, 4200, 4800]:
    im = Image.open(f'scratch/mobile_slice_{i}.png')
    # check non-white pixel ratio
    pixels = list(im.getdata())
    non_white = sum(1 for p in pixels if p[0] < 245 or p[1] < 245 or p[2] < 245)
    print(f"Slice {i}: non-white pixels = {non_white} / {len(pixels)} ({non_white / len(pixels) * 100:.1f}%)")

