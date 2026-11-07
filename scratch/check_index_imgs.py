import os
from PIL import Image

# Let's inspect index.html to see which archive images were used in the marquee and what they are
with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

import re
matches = re.findall(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*alt=["\']([^"\']*)["\']', idx_content)
print("Index images and alts:")
for src, alt in matches:
    print(f"  {src} -> {alt}")

