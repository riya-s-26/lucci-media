from PIL import Image

p1 = 'C:/Users/riyas/.gemini/antigravity/brain/91a1ccde-d165-4dfe-810e-513091b2e231/.user_uploaded/media_1794227905001_00ef3a0b.png'
im1 = Image.open(p1)

print("Original image mode:", im1.mode)
print("Original image size:", im1.size)

# The user image is 320 x 257.
# It has a grey outer frame box and the logo inside.
# The logo has black text 'LUCCI MEDIA' where I of LUCCI connects with M of MEDIA.
# Let's crop the logo exactly:
im1_rgb = im1.convert('RGB')
pixels = im1_rgb.load()
min_x, min_y, max_x, max_y = im1.width, im1.height, 0, 0
for y in range(im1.height):
    for x in range(im1.width):
        r, g, b = pixels[x, y]
        # Ignore outer box line: look for dark pixels in the inner area
        if r < 100 and g < 100 and b < 100 and 40 < x < im1.width - 25 and 100 < y < 160:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)

print(f"Logo bbox: ({min_x}, {min_y}, {max_x}, {max_y}), size: {max_x - min_x + 1} x {max_y - min_y + 1}")
crop = im1.crop((min_x, min_y, max_x + 1, max_y + 1))
crop.save('scratch/user_ref1_isolated.png')
print("Saved scratch/user_ref1_isolated.png")

