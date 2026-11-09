with open('about.css', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
matches = re.findall(r'(\.[a-zA-Z0-9_-]*(?:img|media|photo|collage)[^{]*\{[^}]*\})', text)
for m in matches:
    if 'filter' in m or 'contrast' in m or 'saturate' in m:
        print(m)

