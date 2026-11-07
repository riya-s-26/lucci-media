from PIL import Image

im_bot04 = Image.open('assets/archive/bot_04.jpg')
im_crop = Image.open('assets/about/how_we_think_camera.jpg')

print("bot_04 size:", im_bot04.size)
print("how_we_think_camera size:", im_crop.size)

# Let's compare average color
c1 = im_bot04.resize((10, 10)).convert('RGB').getdata()
c2 = im_crop.resize((10, 10)).convert('RGB').getdata()
avg1 = [sum(x[i] for x in c1)//100 for i in range(3)]
avg2 = [sum(x[i] for x in c2)//100 for i in range(3)]
print("bot_04 avg:", avg1)
print("crop avg:", avg2)

