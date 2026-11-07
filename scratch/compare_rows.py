from PIL import Image

im_orig = Image.open('scratch/sec3_orig_2x.png')
im_new = Image.open('scratch/test_sec3_rendered.png')

print("Orig size:", im_orig.size)
print("New size:", im_new.size)

# Let's side-by-side compare
w, h = im_orig.size
comp = Image.new('RGB', (w * 2 + 20, h), (240, 240, 240))
comp.paste(im_orig, (0, 0))
comp.paste(im_new, (w + 20, 0))
comp.save('scratch/compare_sec3_rows.png')
print("Saved scratch/compare_sec3_rows.png")

