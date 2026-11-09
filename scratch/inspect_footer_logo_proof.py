from PIL import Image

im = Image.open('scratch/proof_final_footer.png')
# find dark pixels in this crop
min_x, min_y, max_x, max_y = im.width, im.height, 0, 0
pixels = im.load()
for y in range(im.height):
    for x in range(im.width):
        r, g, b = pixels[x, y]
        if r < 50 and g < 50 and b < 50:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)

print(f"Footer dark bbox: ({min_x}, {min_y}, {max_x}, {max_y}), size: {max_x - min_x} x {max_y - min_y}")
if max_x > min_x and max_y > min_y:
    crop = im.crop((min_x, min_y, max_x, max_y))
    crop.save('scratch/proof_footer_logo_cropped.png')
    print("Saved proof_footer_logo_cropped.png with size", crop.size)

