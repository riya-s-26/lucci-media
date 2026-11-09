with open('scratch_luccimedia.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
matches = re.findall(r'https?://[^\s"\'<>]+(?:png|svg|jpg)', text)
print(f"Found {len(matches)} image URLs in scratch_luccimedia.html")
for m in matches:
    if 'logo' in m.lower() or 'brand' in m.lower() or 'lucci' in m.lower() or 'wordmark' in m.lower():
        print("Logo match:", m)

