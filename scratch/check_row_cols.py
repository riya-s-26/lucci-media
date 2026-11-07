from PIL import Image

im = Image.open('scratch/sec3_rows.png')
w, h = im.size

# Let's inspect where the columns are:
# Row 1 is between y=0 and y=36
row1 = im.crop((0, 0, w, 36))
row1.save('scratch/row1_inspect.png')

# Let's find dark pixels horizontally across row1
col_dark = []
for x in range(w):
    dark_in_x = sum(1 for y in range(8, 28) if sum(row1.getpixel((x, y))[:3])/3 < 200)
    col_dark.append(dark_in_x)

# Print where text clusters are
in_cluster = False
clusters = []
c_start = 0
for x, d in enumerate(col_dark):
    if d > 0 and not in_cluster:
        in_cluster = True
        c_start = x
    elif d == 0 and in_cluster:
        in_cluster = False
        if x - c_start > 5:
            clusters.append((c_start, x))

print("Clusters in Row 1:", clusters)

