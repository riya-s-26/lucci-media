from PIL import Image

im = Image.open('scratch/proof_final_header_stacked.png').convert('RGB')
# find all pixels with r < 100
dark_pts = []
for y in range(im.height):
    for x in range(im.width):
        r, g, b = im.getpixel((x, y))
        if r < 100 and g < 100 and b < 100:
            dark_pts.append((x, y))

print(f"Total dark points in header: {len(dark_pts)}")
if dark_pts:
    min_x = min(p[0] for p in dark_pts)
    max_x = max(p[0] for p in dark_pts)
    min_y = min(p[1] for p in dark_pts)
    max_y = max(p[1] for p in dark_pts)
    print(f"Overall header dark bounding box: x in [{min_x}, {max_x}], y in [{min_y}, {max_y}]")

