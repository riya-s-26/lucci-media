from PIL import Image

im = Image.open('assets/lucci-mark-dark.png')
print("lucci-mark-dark size:", im.size)
# inspect alpha and content
alpha = im.split()[-1]
print("lucci-mark-dark bbox:", alpha.getbbox())

