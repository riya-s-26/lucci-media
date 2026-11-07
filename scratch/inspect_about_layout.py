from PIL import Image

im = Image.open(r'C:/Users/riyas/.gemini/antigravity/brain/91a1ccde-d165-4dfe-810e-513091b2e231/.user_uploaded/media_1794049842470_6953d09f.jpg')
w, h = im.size

# Let's inspect background color in different parts
print('BG top-left (x=20, y=80):', im.getpixel((20, 80)))
print('BG center (x=200, y=400):', im.getpixel((200, 400)))
print('BG bottom (x=200, y=900):', im.getpixel((200, 900)))

# Let's inspect text colors
# Hero heading 'WE BUILD'
print('Hero heading color (x=50, y=105):', im.getpixel((50, 105)))
# Divider lines
# Look at horizontal lines across sections
for y in range(300, 325):
    line_p = [im.getpixel((x, y))[0] for x in range(30, w-30, 10)]
    avg = sum(line_p) / len(line_p)
    if avg < 235:
        print(f'Possible divider line near y={y}, avg={avg:.1f}')

for y in range(500, 525):
    line_p = [im.getpixel((x, y))[0] for x in range(30, w-30, 10)]
    avg = sum(line_p) / len(line_p)
    if avg < 235:
        print(f'Possible divider line near y={y}, avg={avg:.1f}')

for y in range(670, 700):
    line_p = [im.getpixel((x, y))[0] for x in range(30, w-30, 10)]
    avg = sum(line_p) / len(line_p)
    if avg < 235:
        print(f'Possible divider line near y={y}, avg={avg:.1f}')

for y in range(820, 850):
    line_p = [im.getpixel((x, y))[0] for x in range(30, w-30, 10)]
    avg = sum(line_p) / len(line_p)
    if avg < 235:
        print(f'Possible divider line near y={y}, avg={avg:.1f}')

for y in range(980, 1010):
    line_p = [im.getpixel((x, y))[0] for x in range(30, w-30, 10)]
    avg = sum(line_p) / len(line_p)
    if avg < 235:
        print(f'Possible divider line near y={y}, avg={avg:.1f}')

