with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
tags = re.findall(r'<img[^>]+>', text)
for tag in tags:
    src_m = re.search(r'src=["\']([^"\']+)["\']', tag)
    alt_m = re.search(r'alt=["\']([^"\']*)["\']', tag)
    if src_m:
        src = src_m.group(1)
        alt = alt_m.group(1) if alt_m else ''
        print(f"{src:35} -> {alt}")

