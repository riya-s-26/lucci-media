from PIL import Image

im = Image.open('scratch/sec3_rows.png')
w, h = im.size
print("Rows crop size:", w, h)

# Let's find background color
bg = im.getpixel((10, 10))
print("Background color:", bg)

# Let's inspect vertical slices where each row is located
# The rows are separated by horizontal lines
lines_y = []
for y in range(h):
    # sample across x=20..w-20
    dark_count = sum(1 for x in range(20, w-20) if sum(im.getpixel((x, y))[:3])/3 < 220)
    if dark_count > (w - 40) * 0.7:
        lines_y.append(y)

print("Detected divider lines at y offsets:", lines_y)

