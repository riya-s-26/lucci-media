from PIL import Image

im = Image.open('scratch/team_section_crop.png')
# let's save a resized overview of team_section_crop
small = im.resize((720, int(im.height * 720 / im.width)))
small.save('scratch/team_section_overview.png')

# Let's inspect where any non-(253,253,252) pixel is in team_section_crop
bg = (253, 253, 252)
non_bg_x = [x for x in range(im.width) for y in range(im.height) if im.getpixel((x, y)) != bg]
if non_bg_x:
    print(f"X bounds of team content: [{min(non_bg_x)}, {max(non_bg_x)}]")

# Also let's inspect where Nicole and Deandra are
# Scan row by row between y=200 and y=500
for y in range(200, 500, 50):
    row_pixels = [im.getpixel((x, y)) for x in range(im.width)]
    # count non-bg in 4 quadrants across x: [100, 410], [410, 720], [720, 1030], [1030, 1340]
    q1 = sum(1 for p in row_pixels[100:410] if p != bg)
    q2 = sum(1 for p in row_pixels[410:720] if p != bg)
    q3 = sum(1 for p in row_pixels[720:1030] if p != bg)
    q4 = sum(1 for p in row_pixels[1030:1340] if p != bg)
    print(f"y={y}: Q1={q1}, Q2={q2}, Q3={q3}, Q4={q4}")

