from PIL import Image

p2 = 'C:/Users/riyas/.gemini/antigravity/brain/91a1ccde-d165-4dfe-810e-513091b2e231/.user_uploaded/media_1794227908304_44957956.png'
im2 = Image.open(p2)
# find non-white/black bounding box
# Let's inspect rgb
print("Ref 2 mode:", im2.mode)
# If RGBA or RGB
im2_rgb = im2.convert('RGB')
bbox2 = [None, None, None, None]
# find bounding box of black pixels (< 50)
pixels = im2_rgb.load()
min_x, min_y, max_x, max_y = im2.width, im2.height, 0, 0
for y in range(im2.height):
    for x in range(im2.width):
        r, g, b = pixels[x, y]
        if r < 100 and g < 100 and b < 100:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)

print(f"Ref 2 logo bbox: ({min_x}, {min_y}, {max_x}, {max_y}), size: {max_x - min_x} x {max_y - min_y}")
logo2_crop = im2.crop((min_x, min_y, max_x + 1, max_y + 1))
print("Aspect ratio of Ref 2 stacked logo:", logo2_crop.width / logo2_crop.height)

# Now check assets/lucci-client-logo-black.png
im_proj = Image.open('assets/lucci-client-logo-black.png')
alpha = im_proj.split()[-1]
bbox_proj = alpha.getbbox()
print("Project stacked logo bbox:", bbox_proj)
crop_proj = im_proj.crop(bbox_proj)
print("Aspect ratio of project stacked logo:", crop_proj.width / crop_proj.height)

