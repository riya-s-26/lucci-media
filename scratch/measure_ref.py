from PIL import Image

# Let's inspect Reference Image 1 (media_1794049842470_6953d09f.jpg) to measure column alignment
p = r'C:\Users\riyas\.gemini\antigravity\brain\91a1ccde-d165-4dfe-810e-513091b2e231\.user_uploaded\media_1794049842470_6953d09f.jpg'
im = Image.open(p)
w, h = im.size
print(f"Ref Image 1 size: {w} x {h}")

# Let's find left margin of header logo, hero text, section numbers, etc.
# The image width is 682.
# Let's crop vertical slices at x=20..80 to see where content starts
slice_left = im.crop((0, 0, 100, h))
slice_left.save('scratch/ref_left_gutter.png')
print("Saved scratch/ref_left_gutter.png")

