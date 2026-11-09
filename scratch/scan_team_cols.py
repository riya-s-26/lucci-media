from PIL import Image

im = Image.open('scratch/final_proof_team_section.png').convert('RGB')
# scan columns
col_dark = []
for x in range(im.width):
    d = sum(1 for y in range(im.height) if im.getpixel((x, y))[0] < 50)
    col_dark.append(d)

for x in range(0, im.width, 20):
    print(f"x={x:4d}: dark = {col_dark[x]:3d}")

