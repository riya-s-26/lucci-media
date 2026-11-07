# Let's inspect Showit html (scratch_luccimedia.html) to see where about_portrait.jpg or other images came from!
with open('scratch_luccimedia.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
matches = re.findall(r'<img[^>]+>', text)
print(f"Total img tags in scratch_luccimedia.html: {len(matches)}")
for m in matches[:25]:
    print(m[:120])

