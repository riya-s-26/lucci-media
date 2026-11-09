from PIL import Image

p1 = 'C:/Users/riyas/.gemini/antigravity/brain/91a1ccde-d165-4dfe-810e-513091b2e231/.user_uploaded/media_1794227905001_00ef3a0b.png'
im1 = Image.open(p1)
im1_rgb = im1.convert('RGB')
pixels = im1_rgb.load()
min_x, min_y, max_x, max_y = im1.width, im1.height, 0, 0
for y in range(im1.height):
    for x in range(im1.width):
        r, g, b = pixels[x, y]
        if r < 100 and g < 100 and b < 100:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)

print(f"Ref 1 horizontal logo bbox: ({min_x}, {min_y}, {max_x}, {max_y}), size: {max_x - min_x} x {max_y - min_y}")
logo1_crop = im1.crop((min_x, min_y, max_x + 1, max_y + 1))
print("Aspect ratio of Ref 1 horizontal logo:", logo1_crop.width / logo1_crop.height)
logo1_crop.save('scratch/ref1_cropped.png')
print("Saved scratch/ref1_cropped.png")

