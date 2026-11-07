from PIL import Image

im = Image.open('scratch/sec3_detail.png')
w, h = im.size

# Let's crop:
# 1. Left side: the heading "[ WHAT WORKING WITH US FEELS LIKE ]" and "WHAT WORKING WITH US FEELS LIKE."
heading_crop = im.crop((0, 0, 270, h))
heading_crop.save('scratch/sec3_heading.png')

# 2. Right side: the 4 rows
rows_crop = im.crop((270, 0, w, h))
rows_crop.save('scratch/sec3_rows.png')

print("Saved sec3_heading.png and sec3_rows.png")

