from PIL import Image

def find_inner_box(img, bg_thresh=250):
    # Analyze row and col brightness to find where photo begins and ends
    w, h = img.size
    gray = img.convert('L')
    
    # Let's inspect borders
    print(f"Image size: {w}x{h}")

hero = Image.open(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\hero_region.jpg")
print("Hero region:", hero.size)

who = Image.open(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\who_region.jpg")
print("Who region:", who.size)

# Let's inspect mockup at (225, 36)
m = Image.open(r"C:\Users\ekta bansal\.gemini\antigravity\brain\f5f3c267-89c4-44aa-8b83-5fc2de891e69\.user_uploaded\media_1795430504285_53187fb7.jpg")

# Let's sample pixels around the hero box
# Hero is to the right of text. Left concept width is roughly 512.
# Let's check x=220..235, y=30..45
for y in range(30, 45):
    p = m.getpixel((230, y))
    # print when color changes from near white (255,255,255)
# Let's print the bounding box detection
# Background is white (255, 255, 255) or off-white.
# Find where pixel is not white in the region x: 220-495, y: 30-240
left, top, right, bottom = 1000, 1000, 0, 0
for x in range(220, 500):
    for y in range(30, 240):
        r, g, b = m.getpixel((x, y))
        # If not pure white / page background
        if r < 240 or g < 240 or b < 240:
            if x < left: left = x
            if x > right: right = x
            if y < top: top = y
            if y > bottom: bottom = y

print(f"Hero box detected: left={left}, top={top}, right={right}, bottom={bottom}, width={right-left}, height={bottom-top}")

# Same for who box: x in [15, 250], y in [295, 420]
w_left, w_top, w_right, w_bottom = 1000, 1000, 0, 0
for x in range(15, 250):
    for y in range(295, 420):
        r, g, b = m.getpixel((x, y))
        if r < 245 or g < 245 or b < 245:
            if x < w_left: w_left = x
            if x > w_right: w_right = x
            if y < w_top: w_top = y
            if y > w_bottom: w_bottom = y

print(f"Who box detected: left={w_left}, top={w_top}, right={w_right}, bottom={w_bottom}, width={w_right-w_left}, height={w_bottom-w_top}")
