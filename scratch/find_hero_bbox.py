from PIL import Image

im = Image.open(r'C:\Users\riyas\.gemini\antigravity\brain\91a1ccde-d165-4dfe-810e-513091b2e231\.user_uploaded\media_1794049842470_6953d09f.jpg').convert('RGB')
w, h = im.size

# The background of the mockup is off-white (#FDFDFC or similar, r,g,b > 245)
# Let's find where the hero image begins and ends
# In the region x=280..682, y=40..280:
# find bounding box where pixels deviate from the off-white background
bg_r, bg_g, bg_b = im.getpixel((100, 100))
print(f"Mockup background color at (100,100): ({bg_r}, {bg_g}, {bg_b})")

min_x, min_y, max_x, max_y = w, h, 0, 0
for x in range(280, w):
    for y in range(45, 280):
        r, g, b = im.getpixel((x, y))
        diff = abs(r - bg_r) + abs(g - bg_g) + abs(b - bg_b)
        if diff > 30: # significantly different from bg
            if x < min_x: min_x = x
            if x > max_x: max_x = x
            if y < min_y: min_y = y
            if y > max_y: max_y = y

print(f"Hero image bounding box: x1={min_x}, y1={min_y}, x2={max_x}, y2={max_y}")
print(f"Dimensions: width = {max_x - min_x + 1}, height = {max_y - min_y + 1}")

