from PIL import Image

im = Image.open('review/desktop_about.png')
print("Desktop screenshot size:", im.size)

# Scan from top to bottom and find all regions with dark text/elements
for y in range(0, im.height, 200):
    row_dark = sum(1 for x in range(0, im.width, 5) if im.getpixel((x, y))[0] < 100)
    print(f"y={y}: dark count = {row_dark}")

