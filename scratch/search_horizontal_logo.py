import os
import re

for root, dirs, files in os.walk('.'):
    for f in files:
        p = os.path.join(root, f)
        if f.endswith(('.html', '.css', '.js', '.json', '.txt', '.php')):
            try:
                with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                    c = fp.read()
                    if 'horizontal' in c.lower() or 'stacked' in c.lower() or 'branding' in c.lower():
                        print(f"Match in {p}")
            except:
                pass

