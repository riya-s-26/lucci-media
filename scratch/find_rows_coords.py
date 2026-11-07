from PIL import Image

im = Image.open('scratch/sec3_exact_content.png').convert('RGB')
w, h = im.size

# Let's inspect rows area: x=600..1300
# Dividers in y:
divs = []
for y in range(h):
    # sample across x=650..1250
    dark_pix = sum(1 for x in range(650, 1250) if sum(im.getpixel((x, y)))/3 < 225)
    if dark_pix > 400:
        divs.append(y)

print("Divider lines y in sec3_exact_content:", divs)

# Sample x boundaries:
# Number starts, Heading starts, Desc starts, Right margin

