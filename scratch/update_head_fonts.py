import os, re

base = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media"

html_files = [
  'social-media-management-boston.html',
  'beauty-content-creation-boston.html',
  'brand-photography-boston.html',
  'beauty-campaign-production.html',
  'beauty-campaign-production/index.html',
  'beauty-brand-identity-design.html',
  'beauty-brand-identity-design/index.html',
  'med-spa-website-design.html',
  'med-spa-website-design/index.html',
  'google-business-profile-management.html',
  'google-business-profile-management/index.html'
]

for rel in html_files:
    path = os.path.join(base, rel.replace('/', os.sep))
    if not os.path.exists(path):
        print(f"Not found: {rel}")
        continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'Nothing+You+Could+Do' in content or 'Nothing You Could Do' in content:
        print(f"Already has font in head: {rel}")
        continue
    
    # Replace the Google fonts link with one that includes Nothing+You+Could+Do
    # Look for family=Playfair+Display...
    if 'family=Playfair+Display' in content:
        content = re.sub(
            r'family=Playfair\+Display',
            r'family=Nothing+You+Could+Do&family=Playfair+Display',
            content,
            count=1
        )
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated Google font link: {rel}")
    else:
        print(f"No Playfair link found: {rel}")
