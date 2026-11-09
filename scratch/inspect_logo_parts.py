from PIL import Image

im = Image.open('assets/lucci-client-logo-black.png')
print("Dimensions:", im.size)

# The image is 1316 x 688.
# Let's inspect where LUCCI is and where MEDIA is
# Let's crop upper half (LUCCI) and lower half (MEDIA)
w, h = im.size
top_half = im.crop((0, 0, w, h // 2))
bot_half = im.crop((0, h // 2, w, h))

top_bbox = top_half.getbbox()
bot_bbox = bot_half.getbbox()

print("LUCCI bbox in top half:", top_bbox)
print("MEDIA bbox in bot half:", bot_bbox)

