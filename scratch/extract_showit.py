import re
import os

with open('scratch_luccimedia.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

showit_imgs = set(re.findall(r'(?:https?:)?//static\.showit\.co/[^\s"\'\)\>]+', text))
print('Unique Showit URLs in scratch_luccimedia.html:', len(showit_imgs))
for img in sorted(showit_imgs):
    if any(ext in img.lower() for ext in ['.jpg', '.jpeg', '.png', '.webp']):
        print(img)

