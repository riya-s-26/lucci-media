from PIL import Image

im = Image.open('scratch/sec3_full_2x.png')
w, h = im.size

# Let's inspect where the divider lines are across y=0..h
# In x=600..1200:
dividers = []
for y in range(h):
    dark_count = sum(1 for x in range(650, 1250) if sum(im.getpixel((x, y)))/3 < 225)
    if dark_count > 500:
        dividers.append(y)

print("Dividers in sec3_full_2x (relative to y=1300):", dividers)

