from PIL import Image

# Let's inspect the two candidates placed in the hero box of media_1794049842470_6953d09f.jpg
ref = Image.open(r'C:\Users\riyas\.gemini\antigravity\brain\91a1ccde-d165-4dfe-810e-513091b2e231\.user_uploaded\media_1794049842470_6953d09f.jpg').convert('RGB')
w, h = ref.size

# Hero box is at x1=280, y1=45, x2=681, y2=279 (width=402, height=235)
box_w = 402
box_h = 235

# Option A: Professional content shoot (lucci-bts-shoot.jpg)
bts_im = Image.open('scratch/hero_opt_bts_shoot.png')
opt_a = ref.copy()
opt_a.paste(bts_im, (280, 45))
opt_a.save('scratch/mockup_opt_a_bts.png')

# Option B: Skincare products (product-content.webp)
prod_im = Image.open('scratch/hero_opt_skincare_products.png')
opt_b = ref.copy()
opt_b.paste(prod_im, (280, 45))
opt_b.save('scratch/mockup_opt_b_prod.png')

# Option C: Camera monitor filming treatment (bot_04.jpg)
bot4_im = Image.open('scratch/hero_opt_camera_monitor.png')
opt_c = ref.copy()
opt_c.paste(bot4_im, (280, 45))
opt_c.save('scratch/mockup_opt_c_monitor.png')

print("Generated mockup options A, B, and C.")

