from PIL import Image

im = Image.open('scratch/sec3_rows.png')
w, h = im.size

# Total height is 145.
# With 4 rows, each row is approximately 32-35 pixels high
for i in range(4):
    y1 = int(i * (h / 4))
    y2 = int((i + 1) * (h / 4))
    row = im.crop((0, y1, w, y2))
    row.save(f'scratch/row_{i+1}.png')
    print(f"Row {i+1} y={y1}..{y2}")

