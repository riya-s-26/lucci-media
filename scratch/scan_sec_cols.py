from PIL import Image

im = Image.open(r'C:\Users\riyas\.gemini\antigravity\brain\91a1ccde-d165-4dfe-810e-513091b2e231\.user_uploaded\media_1794049842470_6953d09f.jpg').convert('L')
w, h = im.size

# Let's inspect where the main content begins after the section number (x > 70)
for name, y in [
    ('Section .01 image', 340),
    ('Section .02 heading', 520),
    ('Section .03 heading', 700),
    ('Section .04 founder img', 850),
]:
    # scan x from 60 to 200
    first_dark = None
    for x in range(65, 200):
        if im.getpixel((x, y)) < 150:
            first_dark = x
            break
    print(f"{name:25} at y={y}: starts at x = {first_dark}")

