from PIL import Image

im = Image.open('scratch/sec3_full_2x.png')
w, h = im.size

# Crop Section 03 content area
crop_content = im.crop((0, 30, w, 270))
crop_content.save('scratch/sec3_exact_content.png')
print("Saved sec3_exact_content.png size:", crop_content.size)

