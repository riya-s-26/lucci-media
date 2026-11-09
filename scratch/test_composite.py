from PIL import Image

im = Image.open('assets/lucci-client-logo-black.png')
lucci = im.crop((29, 0, 1258, 344))
media = im.crop((0, 344, 1316, 688))

# In Ref 1, LUCCI width is ~118px out of 249px (~47.4% of total width).
# If we align MEDIA right where LUCCI's I connects to M:
# In master, LUCCI is 1229px wide, MEDIA is 1316px wide.
# In MEDIA, the M starts at x=0. The left diagonal of M starts at x=0.
# If LUCCI and MEDIA meet where I of LUCCI connects with M of MEDIA:
# The I of LUCCI is at the right end of LUCCI (x=1140 to 1229).
# If M is placed at x = 1140:
total_w = 1140 + media.width
horiz_joined = Image.new('RGBA', (total_w, 344), (0, 0, 0, 0))
horiz_joined.paste(lucci, (0, 0))
# paste media on top with alpha composite
horiz_joined = Image.alpha_composite(horiz_joined, Image.new('RGBA', (total_w, 344), (0, 0, 0, 0)))
# paste media at x=1140
m_layer = Image.new('RGBA', (total_w, 344), (0, 0, 0, 0))
m_layer.paste(media, (1140, 0))
final_composite = Image.alpha_composite(horiz_joined, m_layer)
print("Final composite size:", final_composite.size)
print("Aspect ratio:", final_composite.width / final_composite.height)
final_composite.save('scratch/test_interlocking_logo.png')

