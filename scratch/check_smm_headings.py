import re

with open(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\social-media-management-boston.html", 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if re.search(r'<h[1-6]', line, re.I):
        print(f"Line {i+1}: {line.strip()[:100]}")
