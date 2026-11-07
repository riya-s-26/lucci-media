from PIL import Image

# Update assets/about/hero_lex.jpg with the professional beauty content-production photograph
im_hero = Image.open('assets/lucci/lucci-bts-shoot.jpg')
w, h = im_hero.size
target_ratio = 16 / 10
crop_h = int(w / target_ratio)
start_y = (h - crop_h) // 2
hero_crop = im_hero.crop((0, start_y, w, start_y + crop_h)).resize((1200, 750), Image.Resampling.LANCZOS)
hero_crop.save('assets/about/hero_lex.jpg', quality=95)
print("Updated assets/about/hero_lex.jpg with professional beauty content-production photograph.")

