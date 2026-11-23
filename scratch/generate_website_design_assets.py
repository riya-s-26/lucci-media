import os
from PIL import Image, ImageFilter, ImageEnhance

mockup_path = r"C:\Users\ekta bansal\.gemini\antigravity\brain\f5f3c267-89c4-44aa-8b83-5fc2de891e69\.user_uploaded\media_1795430504285_53187fb7.jpg"
out_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\assets\services"

m_img = Image.open(mockup_path).convert('RGB')
print(f"Loaded mockup: {m_img.size}")

# 1. Hero image crop:
# In mockup Concept 1 (left half), the laptop photo is bounded by (225, 36, 488, 230)
# Let's inspect exact border boundaries:
hero_crop = m_img.crop((225, 36, 488, 230))
print(f"Hero crop source size: {hero_crop.size}")

# Resize to 1080x760 for @2x and 540x380 for 1x
hero_2x = hero_crop.resize((1080, 760), Image.Resampling.LANCZOS)
# Gentle enhancement for sharpness
enhancer = ImageEnhance.Sharpness(hero_2x)
hero_2x = enhancer.enhance(1.25)
hero_1x = hero_2x.resize((540, 380), Image.Resampling.LANCZOS)

hero_1x_path = os.path.join(out_dir, "website-design-hero.jpg")
hero_2x_path = os.path.join(out_dir, "website-design-hero@2x.jpg")

hero_1x.save(hero_1x_path, "JPEG", quality=92, optimize=True)
hero_2x.save(hero_2x_path, "JPEG", quality=90, optimize=True)
print(f"Saved: {hero_1x_path} ({os.path.getsize(hero_1x_path)} bytes)")
print(f"Saved: {hero_2x_path} ({os.path.getsize(hero_2x_path)} bytes)")

# 2. Who It's For image crop:
# In mockup Concept 1, the smartphone photo is bounded by (24, 305, 236, 410)
# Notice the aspect ratio of 212x105 is roughly 2:1, but the target layout box is 480x360 (4:3) or 480x300.
# Let's check how much vertical context or padding exists, or crop nicely and fit into 480x360 or 480x320.
# Let's crop (24, 300, 236, 412)
who_crop = m_img.crop((24, 300, 236, 412))
print(f"Who crop source size: {who_crop.size}")

# For the 480x360 container (or 960x720 @2x), we can resize to 960x508 or center-crop/fit:
who_2x = who_crop.resize((960, 720), Image.Resampling.LANCZOS)
enhancer_who = ImageEnhance.Sharpness(who_2x)
who_2x = enhancer_who.enhance(1.2)
who_1x = who_2x.resize((480, 360), Image.Resampling.LANCZOS)

who_1x_path = os.path.join(out_dir, "website-design-who.jpg")
who_2x_path = os.path.join(out_dir, "website-design-who@2x.jpg")

who_1x.save(who_1x_path, "JPEG", quality=92, optimize=True)
who_2x.save(who_2x_path, "JPEG", quality=90, optimize=True)
print(f"Saved: {who_1x_path} ({os.path.getsize(who_1x_path)} bytes)")
print(f"Saved: {who_2x_path} ({os.path.getsize(who_2x_path)} bytes)")

print("Successfully generated all Website Design assets!")
