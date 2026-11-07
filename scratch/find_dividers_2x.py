from PIL import Image

im = Image.open('scratch/sec3_orig_2x.png')
w, h = im.size
print("sec3_orig_2x size:", w, h)

# Let's find divider line positions y in sec3_orig_2x
dividers = []
for y in range(h):
    # check line across x=100..w-50
    dark_pix = sum(1 for x in range(100, w-50) if sum(im.getpixel((x, y)))/3 < 235)
    if dark_pix > (w - 150) * 0.8:
        dividers.append(y)

print("Dividers found at relative y:", dividers)

