import subprocess

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
file_url = "file:///C:/xampp/htdocs/luci/about.html"

# Run chrome with DevTools Protocol or JS evaluation
# Let's inspect CSS in about.css for .about-team-
with open('about.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'(\.about-team[^{]*\{[^}]*\})', text)
for m in matches:
    print(m)

