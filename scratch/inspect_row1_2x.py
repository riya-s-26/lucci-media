from PIL import Image

im = Image.open('scratch/sec3_orig_2x.png')
w, h = im.size

# Let's inspect x=0..w, and see where the text starts
# Let's find first dark pixel in x
for x in range(0, w, 5):
    dark = sum(1 for y in range(h) if sum(im.getpixel((x, y)))/3 < 200)
    if dark > 5:
        print(f"Text starts around relative x = {x}")
        break

# Let's find where the 3 columns are:
# sample row 1 (y=20..70)
row1 = im.crop((0, 15, w, 75))
row1.save('scratch/row1_2x.png')
print("Saved row1_2x.png")

