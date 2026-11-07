from PIL import Image

im = Image.open('scratch/sec3_exact_content.png').convert('L')
w, h = im.size

# In Row 1 (y=10..50), let's inspect where dark pixels are across x=550..1320
row1_dark = [sum(1 for y in range(12, 45) if im.getpixel((x, y)) < 210) for x in range(550, 1320)]

clusters = []
in_c = False
start_x = 0
for i, d in enumerate(row1_dark):
    x = 550 + i
    if d > 2 and not in_c:
        in_c = True
        start_x = x
    elif d <= 2 and in_c:
        in_c = False
        if x - start_x > 3:
            clusters.append((start_x, x))

print("Row 1 x-clusters:", clusters)

