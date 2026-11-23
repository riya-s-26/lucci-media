from PIL import Image

full = Image.open(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\render_web_full.png")
print("Full page image size:", full.size)

# Save smaller preview of full page
preview = full.resize((720, 1400), Image.Resampling.LANCZOS)
preview.save(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\web_full_preview.jpg", quality=85)
print("Saved web_full_preview.jpg")

# Slices of individual sections:
# 1. Hero
hero = full.crop((0, 0, 1440, 650))
hero.save(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\sec1_hero.jpg")

# 2. What's Included
included = full.crop((0, 650, 1440, 1000))
included.save(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\sec2_included.jpg")

# 3. Who It's For + How It Works + Investment
details = full.crop((0, 1000, 1440, 1600))
details.save(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\sec3_details.jpg")

# 4. FAQ + Mid CTA + Bottom Banner
bottom = full.crop((0, 1600, 1440, 2400))
bottom.save(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\sec4_bottom.jpg")

print("All sections sliced and verified!")
