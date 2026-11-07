import re

with open('scratch/luccimedia.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

imgs = re.findall(r'//static\.showit\.co/[^\s"\'\)]+', text)
print('Unique Showit images in luccimedia.html:', len(set(imgs)))
for img in sorted(list(set(imgs)))[:40]:
    print(img)
