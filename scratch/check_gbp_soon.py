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
    
    matches = re.findall(r'google-business-profile-management[\s\S]{1,150}?COMING SOON', c)
    if matches:
        found.append((os.path.relpath(f, base_dir), matches))

print(f"Files where google-business-profile-management is associated with COMING SOON: {len(found)}")
for f, m in found:
    print(f, m)
