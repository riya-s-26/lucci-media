from PIL import Image

im = Image.open('scratch/user_ref1_isolated.png').convert('RGB')
pixels = im.load()

# Count dark pixels per column
col_counts = []
for x in range(im.width):
    cnt = sum(1 for y in range(im.height) if pixels[x, y][0] < 100)
    col_counts.append(cnt)

print("Column counts:")
for x in range(0, im.width, 5):
    print(f"x={x:3d}: {col_counts[x]:2d}")

