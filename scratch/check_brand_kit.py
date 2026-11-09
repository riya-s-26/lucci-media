with open('scratch_luccimedia.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
# check fonts in scratch_luccimedia.html
fonts = re.findall(r'font-family:[^;]+', text, re.IGNORECASE)
print("Unique font families in scratch_luccimedia:")
for f in set(fonts):
    print(" ", f)

# check colors
colors = re.findall(r'rgba?\([^)]+\)|#[0-9a-fA-F]{3,8}', text)
print("\nColor counts:")
from collections import Counter
c = Counter(colors)
for col, cnt in c.most_common(15):
    print(f"  {col}: {cnt}")

