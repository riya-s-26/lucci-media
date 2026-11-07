from PIL import Image

im = Image.open('assets/about/about_portrait.jpg')
print("about_portrait.jpg dimensions:", im.size)
# Let's crop upper half and describe
w, h = im.size
print("Aspect ratio:", w/h)

