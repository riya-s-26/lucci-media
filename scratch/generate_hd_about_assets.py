import os
from PIL import Image, ImageEnhance

os.makedirs('assets/about', exist_ok=True)

# 1. hero_lex.jpg from assets/lucci/lex-studio-pose.jpg
im_hero = Image.open('assets/lucci/lex-studio-pose.jpg')
w, h = im_hero.size
# target 16:10 -> w x int(w / 1.6) = 1200 x 750
target_w, target_h = 1200, 750
crop_h = int(w / (16/10)) # 750
# focus slightly above center so face and upper body are well framed
start_y = int(h * 0.08)
crop_hero = im_hero.crop((0, start_y, w, start_y + crop_h)).resize((target_w, target_h), Image.Resampling.LANCZOS)
crop_hero.save('assets/about/hero_lex.jpg', quality=95)
print("Saved assets/about/hero_lex.jpg:", crop_hero.size)

# 2. story_treatment_room.jpg from media_1794049842470_6953d09f.jpg (enhanced)
ref = Image.open(r'C:\Users\riyas\.gemini\antigravity\brain\91a1ccde-d165-4dfe-810e-513091b2e231\.user_uploaded\media_1794049842470_6953d09f.jpg')
# box: x1=92, y1=304, x2=318, y2=475 in reference image
box_room = (92, 304, 318, 475)
crop_room = ref.crop(box_room)
# resize to 1000x750 with lanczos
crop_room_hd = crop_room.resize((1000, 755), Image.Resampling.LANCZOS)
# slightly enhance brightness and contrast to look luminous and warm
enhancer = ImageEnhance.Brightness(crop_room_hd)
crop_room_hd = enhancer.enhance(1.04)
crop_room_hd.save('assets/about/story_treatment_room.jpg', quality=95)
print("Saved assets/about/story_treatment_room.jpg:", crop_room_hd.size)

# 3. story_bottles.jpg from assets/product-content.webp
im_prod = Image.open('assets/product-content.webp')
# crop center region with bottles on sandstone
pw, ph = im_prod.size
crop_prod = im_prod.crop((0, int(ph * 0.1), pw, int(ph * 0.85))).resize((800, 680), Image.Resampling.LANCZOS)
crop_prod.save('assets/about/story_bottles.jpg', quality=95)
print("Saved assets/about/story_bottles.jpg:", crop_prod.size)

# 4. story_cream.jpg from assets/archive/bot_09.jpg
im_cream = Image.open('assets/archive/bot_09.jpg')
cw, ch = im_cream.size
# crop cream swatch region (centered, slightly down)
box_cream = (int(cw * 0.15), int(ch * 0.25), int(cw * 0.85), int(ch * 0.85))
crop_cream = im_cream.crop(box_cream).resize((800, 680), Image.Resampling.LANCZOS)
crop_cream.save('assets/about/story_cream.jpg', quality=95)
print("Saved assets/about/story_cream.jpg:", crop_cream.size)

# 5. how_we_think_camera.jpg from assets/archive/bot_04.jpg
im_think = Image.open('assets/archive/bot_04.jpg')
tw, th = im_think.size
think_crop_h = int(tw / (16/10))
think_start_y = (th - think_crop_h) // 2
crop_think = im_think.crop((0, think_start_y, tw, think_start_y + think_crop_h)).resize((1600, 1000), Image.Resampling.LANCZOS)
crop_think.save('assets/about/how_we_think_camera.jpg', quality=95)
print("Saved assets/about/how_we_think_camera.jpg:", crop_think.size)

# 6. team_lex.jpg from assets/hero-lex-portrait.jpg
im_team_lex = Image.open('assets/hero-lex-portrait.jpg')
lxw, lxh = im_team_lex.size
team_crop_h = int(lxw / (3/4))
team_start_y = int(lxh * 0.05)
crop_team_lex = im_team_lex.crop((0, team_start_y, lxw, team_start_y + team_crop_h)).resize((1200, 1600), Image.Resampling.LANCZOS)
crop_team_lex.save('assets/about/team_lex.jpg', quality=95)
print("Saved assets/about/team_lex.jpg:", crop_team_lex.size)

# 7. team_studio_chair.jpg from assets/lucci/lucci-bts-shoot.jpg
im_bts = Image.open('assets/lucci/lucci-bts-shoot.jpg')
bw, bh = im_bts.size
bts_crop_h = int(bw / (16/10))
bts_start_y = (bh - bts_crop_h) // 2
crop_bts = im_bts.crop((0, bts_start_y, bw, bts_start_y + bts_crop_h)).resize((1200, 750), Image.Resampling.LANCZOS)
crop_bts.save('assets/about/team_studio_chair.jpg', quality=95)
print("Saved assets/about/team_studio_chair.jpg:", crop_bts.size)

# 8. team_laptop.jpg from assets/archive/top_13.jpg
im_team_collab = Image.open('assets/archive/top_13.jpg')
clw, clh = im_team_collab.size
collab_crop_h = int(clw / (16/10))
collab_start_y = int(clh * 0.15)
crop_collab = im_team_collab.crop((0, collab_start_y, clw, collab_start_y + collab_crop_h)).resize((1200, 750), Image.Resampling.LANCZOS)
crop_collab.save('assets/about/team_laptop.jpg', quality=95)
print("Saved assets/about/team_laptop.jpg:", crop_collab.size)

print("\nAll 8 About page assets generated in high resolution!")

