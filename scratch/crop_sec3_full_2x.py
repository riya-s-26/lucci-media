from PIL import Image

ref = Image.open(r'C:\Users\riyas\.gemini\antigravity\brain\91a1ccde-d165-4dfe-810e-513091b2e231\.user_uploaded\media_1794049842470_6953d09f.jpg')
ref_2x = ref.resize((1364, 2048), Image.Resampling.LANCZOS)

# Let's crop Section 03 entirely: from x=0 to 1364, y=1300 to 1650
sec3_full = ref_2x.crop((0, 1300, 1364, 1650))
sec3_full.save('scratch/sec3_full_2x.png')
print("Saved sec3_full_2x.png size:", sec3_full.size)

