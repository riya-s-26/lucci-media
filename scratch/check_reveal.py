with open('styles.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'\[data-reveal\][^{]*\{[^}]*\}', text)
for m in matches:
    print(m)

