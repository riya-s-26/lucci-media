import os
import glob

html_files = glob.glob(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\**\*.html", recursive=True)
print(f"Total HTML files: {len(html_files)}")

# Check which ones contain 'med-spa-website-design.html' and 'COMING SOON'
soon_count = 0
for f in html_files:
    # Skip scratch
    if "scratch" in f or "review" in f:
        continue
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        content = fp.read()
    if 'med-spa-website-design.html' in content and 'COMING SOON' in content:
        soon_count += 1
        print("Contains soon for website design:", os.path.relpath(f, r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media"))

print(f"Total files with COMING SOON for website design: {soon_count}")
