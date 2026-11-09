from PIL import Image

# Open the source logo
im = Image.open('assets/lucci-client-logo-black.png')
print("Source size:", im.size)

# LUCCI is in top half: y=0 to 344
# MEDIA is in bottom half: y=344 to 688
top = im.crop((0, 0, im.width, 344))
bot = im.crop((0, 344, im.width, im.height))

lucci_box = top.split()[-1].getbbox()
media_box = bot.split()[-1].getbbox()

print("LUCCI bbox:", lucci_box)
print("MEDIA bbox:", media_box)

lucci = top.crop(lucci_box)
media = bot.crop(media_box)

print("LUCCI trimmed size:", lucci.size)
print("MEDIA trimmed size:", media.size)

