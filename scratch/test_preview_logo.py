from PIL import Image

im = Image.open('assets/lucci-horizontal-logo-black.png')
print("Horizontal logo size:", im.size)
# create a preview with off-white background
bg = Image.new('RGB', (im.width + 100, im.height + 100), (253, 253, 252))
bg.paste(im, (50, 50), mask=im.split()[-1])
bg.save('scratch/preview_horizontal_logo.png')
print("Saved scratch/preview_horizontal_logo.png")

