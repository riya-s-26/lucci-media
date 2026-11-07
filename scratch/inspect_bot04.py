from PIL import Image

im = Image.open('assets/archive/bot_04.jpg')
w, h = im.size
print("Width:", w, "Height:", h)

# Let's crop the center where the monitor is
center_box = (w//4, h//4, 3*w//4, 3*h//4)
crop = im.crop(center_box)
crop.save('scratch/bot_04_center.jpg', quality=85)
print("Saved scratch/bot_04_center.jpg")

