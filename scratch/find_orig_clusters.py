from PIL import Image

im_orig = Image.open('scratch/sec3_orig_2x.png').convert('L')
w, h = im_orig.size

# Let's inspect row 1 y=20..50
# Scan x from 0 to w and find clusters of dark pixels
dark_counts = [sum(1 for y in range(25, 55) if im_orig.getpixel((x, y)) < 210) for x in range(w)]

clusters = []
in_c = False
start_x = 0
for x, d in enumerate(dark_counts):
    if d > 2 and not in_c:
        in_c = True
        start_x = x
    elif d <= 2 and in_c:
        in_c = False
        clusters.append((start_x, x))

print("Original clusters in row 1:", clusters)

