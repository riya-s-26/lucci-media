with open('scratch_luccimedia.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
matches = re.findall(r'[^"\'<>\n]*(?:logo|brandmark|wordmark)[^"\'<>\n]*', text, re.IGNORECASE)
for m in list(set(matches))[:30]:
    print(m.strip())
