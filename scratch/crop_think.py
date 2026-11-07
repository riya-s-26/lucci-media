from PIL import Image

im = Image.open('assets/archive/bot_04.jpg')
w, h = im.size
# Target 16:9 or 16:10
# In bot_04.jpg (2160x2700), the camera monitor is centered
target_w = w
target_h = int(w / (16/10)) # 2160 / 1.6 = 1350
start_y = (h - target_h) // 2

crop_bot4 = im.crop((0, start_y, target_w, start_y + target_h))
crop_bot4.save('scratch/how_we_think_hd.jpg', quality=92)
print("Saved scratch/how_we_think_hd.jpg size:", crop_bot4.size)

