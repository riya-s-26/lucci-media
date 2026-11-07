with open('scratch_luccimedia.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
matches = re.findall(r'//static\.showit\.co/[^\s"\'\)]+', text)
for m in sorted(set(matches)):
    # print filename at end
    parts = m.split('/')
    print(parts[-1], "-->", m)

