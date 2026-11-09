with open('styles.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.finditer(r'logo-wipe', text)
for m in matches:
    print(text[m.start()-50:m.end()+150])

