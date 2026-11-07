from PIL import Image

target_size = (402, 235)

# 1. Professional content shoot: lucci-bts-shoot.jpg
im_bts = Image.open('assets/lucci/lucci-bts-shoot.jpg')
bw, bh = im_bts.size
# crop to 402:235 ratio (1.71)
target_ratio = 402 / 235
crop_h = int(bw / target_ratio)
start_y = (bh - crop_h) // 2
crop_bts = im_bts.crop((0, start_y, bw, start_y + crop_h)).resize(target_size, Image.Resampling.LANCZOS)
crop_bts.save('scratch/hero_opt_bts_shoot.png')

# 2. Skincare products: product-content.webp
im_prod = Image.open('assets/product-content.webp')
pw, ph = im_prod.size
crop_h_prod = int(pw / target_ratio)
start_y_prod = int(ph * 0.2)
crop_prod = im_prod.crop((0, start_y_prod, pw, start_y_prod + crop_h_prod)).resize(target_size, Image.Resampling.LANCZOS)
crop_prod.save('scratch/hero_opt_skincare_products.png')

# 3. Beauty treatment setup: story_treatment_room.jpg
im_treat = Image.open('assets/about/story_treatment_room.jpg')
tw, th = im_treat.size
crop_h_treat = int(tw / target_ratio)
start_y_treat = (th - crop_h_treat) // 2
crop_treat = im_treat.crop((0, start_y_treat, tw, start_y_treat + crop_h_treat)).resize(target_size, Image.Resampling.LANCZOS)
crop_treat.save('scratch/hero_opt_treatment_setup.png')

# 4. Professional content shoot: bot_04 on set filming
im_bot4 = Image.open('assets/archive/bot_04.jpg')
w4, h4 = im_bot4.size
crop_h4 = int(w4 / target_ratio)
start_y4 = (h4 - crop_h4) // 2
crop_bot4 = im_bot4.crop((0, start_y4, w4, start_y4 + crop_h4)).resize(target_size, Image.Resampling.LANCZOS)
crop_bot4.save('scratch/hero_opt_camera_monitor.png')

print("All 4 hero candidate crops generated.")

