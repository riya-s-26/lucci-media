from PIL import Image

im = Image.open(r'C:\Users\riyas\.gemini\antigravity\brain\91a1ccde-d165-4dfe-810e-513091b2e231\.user_uploaded\media_1794049842470_6953d09f.jpg').convert('L')
w, h = im.size

sections = {
    'Header Logo': (0, 60),
    'Hero Text': (60, 280),
    'Section .01': (280, 480),
    'Section .02': (480, 650),
    'Section .03': (650, 800),
    'Section .04': (800, 950),
    'Final CTA': (950, 1024),
}

for name, (y1, y2) in sections.items():
    # find first x where pixel is dark (< 150)
    first_x = None
    for x in range(w):
        for y in range(y1, y2):
            if im.getpixel((x, y)) < 100:
                first_x = x
                break
        if first_x is not None:
            break
    print(f"{name:15} (y={y1}..{y2}): leftmost dark pixel at x = {first_x}")

