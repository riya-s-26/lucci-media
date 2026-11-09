from PIL import Image

im = Image.open('scratch/proof_footer_horizontal.png')
# let's find the black pixels in this crop
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

print(f"Footer logo dark pixels bbox: ({min_x}, {min_y}, {max_x}, {max_y}), size: {max_x - min_x} x {max_y - min_y}")
logo_crop = im.crop((min_x, min_y, max_x, max_y))
logo_crop.save('scratch/proof_footer_logo_isolated.png')
print("Saved scratch/proof_footer_logo_isolated.png")

