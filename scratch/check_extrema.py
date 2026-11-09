from PIL import Image

im = Image.open('review/desktop_about.png')
# get min and max RGB in the image
colors = im.getextrema()
print("Extrema:", colors)

