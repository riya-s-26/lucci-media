with open('scratch/tsa_about.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer('soph', text, re.IGNORECASE)]
for idx in matches:
    print("--- MATCH FOR SOPH ---")
    print(text[max(0, idx-200):min(len(text), idx+300)])

