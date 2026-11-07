from PIL import Image

# Let's inspect media_1794049842470_6953d09f.jpg for Section 2
ref_path = r'C:\Users\riyas\.gemini\antigravity\brain\91a1ccde-d165-4dfe-810e-513091b2e231\.user_uploaded\media_1794049842470_6953d09f.jpg'
ref = Image.open(ref_path)
print("Reference image size:", ref.size)

# Let's check Section 2 coordinates
# Section 2 is roughly around y=300 to y=500
crop_sec2 = ref.crop((0, int(ref.height * 0.28), ref.width, int(ref.height * 0.50)))
crop_sec2.save('scratch/ref_sec2_full.jpg', quality=95)
print("Saved scratch/ref_sec2_full.jpg")

