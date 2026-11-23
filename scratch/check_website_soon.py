import os
import glob
import re

base_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media"
html_files = glob.glob(os.path.join(base_dir, "**", "*.html"), recursive=True)

found = []
for f in html_files:
    if "scratch" in f or "review" in f:
        continue
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    
    # Check if med-spa-website-design is followed within 150 chars by COMING SOON
    matches = re.findall(r'med-spa-website-design[\s\S]{1,150}?COMING SOON', c)
    if matches:
        found.append((os.path.relpath(f, base_dir), matches))

print(f"Files where med-spa-website-design is associated with COMING SOON: {len(found)}")
for f, m in found:
    print(f, m)
