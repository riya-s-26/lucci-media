with open(r'c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\campaign-shoots.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'(--font-[^;]+;)', text)
print("CSS Variables in campaign-shoots.css:")
for m in matches:
    print(" ", m)

rules = re.findall(r'([^{}]*\{[^{}]*font-family:[^{}]*\})', text)
print("\nRules with font-family in campaign-shoots.css:")
for r in rules:
    print(" ", ' '.join(r.split()))
