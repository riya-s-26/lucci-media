from PIL import Image

im = Image.open('scratch/proof_final_header_stacked.png')
# find dark pixels in the header left area (x=0 to 250)
min_x, min_y, max_x, max_y = 250, im.height, 0, 0
pixels = im.load()
for y in range(im.height):
    for x in range(250):
        r, g, b = pixels[x, y]
        if r < 50 and g < 50 and b < 50:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)

print(f"Header logo bbox: ({min_x}, {min_y}, {max_x}, {max_y}), size: {max_x - min_x} x {max_y - min_y}")
if max_x > min_x:
    crop = im.crop((min_x, min_y, max_x, max_y))
    crop.save('scratch/proof_header_logo_isolated.png')
    print("Aspect ratio:", crop.width / crop.height)

