from PIL import Image

im = Image.open('scratch/card_4_text.png')
print("Card 4 text size:", im.size)
# find bounding box of non-bg pixels
non_bg = []
for y in range(im.height):
    for x in range(im.width):
        if im.getpixel((x, y)) != (253, 253, 252):
            non_bg.append((x, y))

if non_bg:
    min_x = min(p[0] for p in non_bg)
    max_x = max(p[0] for p in non_bg)
    min_y = min(p[1] for p in non_bg)
    max_y = max(p[1] for p in non_bg)
    print(f"Non-bg in card 4 text: x=[{min_x}, {max_x}], y=[{min_y}, {max_y}], count={len(non_bg)}")
else:
    print("No non-bg pixels in card 4 text!")

