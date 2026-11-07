from PIL import Image

im = Image.open(r'C:\Users\riyas\.gemini\antigravity\brain\91a1ccde-d165-4dfe-810e-513091b2e231\lucci_media_about_mockup_corrected.png')
w, h = im.size
print("Mockup dimensions:", w, h)

# Check hero region
hero_check = im.crop((280, 45, 682, 280))
hero_check.save('scratch/verify_hero_mockup.png')

# Check Section 03 region
sec3_check = im.crop((0, 660, 682, 805))
sec3_check.save('scratch/verify_sec3_mockup.png')

print("Verification crops generated.")

