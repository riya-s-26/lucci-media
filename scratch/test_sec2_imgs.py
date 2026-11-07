from PIL import Image

# Let's crop a square or 4:3 from product-content.webp and bot_09.jpg
p1 = Image.open('assets/product-content.webp')
p2 = Image.open('assets/archive/bot_09.jpg')

print("product-content size:", p1.size)
print("bot_09 size:", p2.size)

# Sample color of bot_09
rgb_bot9 = p2.convert('RGB').resize((10, 10))
print("bot_09 avg RGB:", [sum(x[i] for x in rgb_bot9.getdata())//100 for i in range(3)])

# Let's crop the cream texture region of bot_09
w, h = p2.size
crop_bot9 = p2.crop((w//4, h//4, 3*w//4, 3*h//4))
print("bot_09 crop avg RGB:", [sum(x[i] for x in crop_bot9.convert('RGB').resize((10,10)).getdata())//100 for i in range(3)])

