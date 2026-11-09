from PIL import Image

im = Image.open('assets/lucci-client-logo-black.png')
top = im.crop((0, 0, im.width, 344))
bot = im.crop((0, 344, im.width, im.height))

lucci = top.crop(top.split()[-1].getbbox())
media = bot.crop(bot.split()[-1].getbbox())

# Let's test spacing:
# In the word LUCCI, letter spacing is approximately 30-40px. A natural word space between LUCCI and MEDIA is ~160px.
gap = 160
total_w = lucci.width + gap + media.width
h = max(lucci.height, media.height)

horiz = Image.new('RGBA', (total_w, h), (0, 0, 0, 0))
horiz.paste(lucci, (0, 0))
horiz.paste(media, (lucci.width + gap, 0))

# Save horizontal logo
horiz.save('assets/lucci-horizontal-logo-black.png')
print("Saved assets/lucci-horizontal-logo-black.png with dimensions:", horiz.size)

# Also generate dark/white version if needed
# For white version:
white = Image.new('RGBA', horiz.size, (0, 0, 0, 0))
r, g, b, a = horiz.split()
white_rgb = Image.new('RGB', horiz.size, (255, 255, 255))
white.paste(white_rgb, mask=a)
white.save('assets/lucci-horizontal-logo-light.png')
print("Saved assets/lucci-horizontal-logo-light.png")

