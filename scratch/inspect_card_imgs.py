from PIL import Image

for i in range(1, 5):
    im = Image.open(f'scratch/card_{i}_visible.png')
    print(f"Card {i} size: {im.size}")
    # find where pixels differ from background
    diff_pixels = [p for p in im.getdata() if p != (253, 253, 252)]
    print(f"Card {i} non-bg pixels: {len(diff_pixels)}")

