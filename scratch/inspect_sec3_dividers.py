from PIL import Image

im = Image.open(r'C:\Users\riyas\.gemini\antigravity\brain\91a1ccde-d165-4dfe-810e-513091b2e231\.user_uploaded\media_1794049842470_6953d09f.jpg')
# Section 03 is between y=660 and y=800
# Let's crop x=0..682, y=660..800
sec3 = im.crop((0, 660, 682, 805))
sec3.save('scratch/sec3_detail.png')
print("Saved scratch/sec3_detail.png")

# Let's check the horizontal divider lines in sec3
# Dividers are thin horizontal lines where y has a horizontal line of pixels darker than background
for y in range(660, 805):
    # check line across x=300..650
    pixels = [im.getpixel((x, y)) for x in range(300, 650)]
    darkness = sum(1 for p in pixels if sum(p[:3])/3 < 235)
    if darkness > 300: # mostly dark line
        print(f"Horizontal divider at y={y}")

