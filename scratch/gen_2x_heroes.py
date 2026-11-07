from PIL import Image

# 2x dimensions: 1364 x 2048
# Hero box: x=560, y=90, w=804, h=470

# Option 1: lucci-bts-shoot.jpg (professional content shoot)
im_bts = Image.open('assets/lucci/lucci-bts-shoot.jpg')
bw, bh = im_bts.size
target_ratio = 804 / 470
crop_h = int(bw / target_ratio)
start_y = (bh - crop_h) // 2
crop_bts_2x = im_bts.crop((0, start_y, bw, start_y + crop_h)).resize((804, 470), Image.Resampling.LANCZOS)
crop_bts_2x.save('scratch/hero_bts_2x.png')

# Option 2: product-content.webp (skincare products)
im_prod = Image.open('assets/product-content.webp')
pw, ph = im_prod.size
crop_h_prod = int(pw / target_ratio)
start_y_prod = int(ph * 0.15)
crop_prod_2x = im_prod.crop((0, start_y_prod, pw, start_y_prod + crop_h_prod)).resize((804, 470), Image.Resampling.LANCZOS)
crop_prod_2x.save('scratch/hero_prod_2x.png')

print("Saved hero_bts_2x.png and hero_prod_2x.png")

