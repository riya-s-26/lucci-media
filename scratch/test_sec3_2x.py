import os
from PIL import Image, ImageDraw, ImageFont

# Let's inspect the exact Section 03 bounding box at 2x scale
# In 1x mockup:
# Section 03 heading on left: x=32..260, y=660..780
# Section 03 rows on right: x=270..650, y=662..798
# Let's crop the Section 03 region at 2x scale and test rendering
ref = Image.open(r'C:\Users\riyas\.gemini\antigravity\brain\91a1ccde-d165-4dfe-810e-513091b2e231\.user_uploaded\media_1794049842470_6953d09f.jpg').convert('RGB')
ref_2x = ref.resize((1364, 2048), Image.Resampling.LANCZOS)

# Rows region at 2x: x=540..1300, y=1320..1605
rows_box = (540, 1320, 1310, 1605)
crop_rows_orig = ref_2x.crop(rows_box)
crop_rows_orig.save('scratch/sec3_orig_2x.png')
print("Saved sec3_orig_2x.png")

