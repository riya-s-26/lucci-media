import os, re

base = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media"

pages = [
  'social-media-management-boston.html',
  'beauty-content-creation-boston.html',
  'brand-photography-boston.html',
  'beauty-campaign-production.html',
  'beauty-brand-identity-design.html',
  'med-spa-website-design.html',
  'google-business-profile-management.html',
  'local-seo-med-spas.html'
]

for p in pages:
    path = os.path.join(base, p)
    print(f"\n=================== {p} ===================")
    if not os.path.exists(path):
        print("  File not found!")
        continue
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # stylesheets
    sheets = re.findall(r'<link[^>]+rel=[\'"]stylesheet[\'"][^>]*>', html)
    for s in sheets:
        print("  Stylesheet:", s)
        
    # headings
    headings = re.findall(r'(<(?:h1|h2|h3|h4|h5|h6)[^>]*>.*?</(?:h1|h2|h3|h4|h5|h6)>)', html, re.DOTALL | re.IGNORECASE)
    print(f"  Total headings: {len(headings)}")
    for h in headings[:10]:
        # print first 100 chars of heading
        clean_h = ' '.join(h.split())
        if len(clean_h) > 100:
            clean_h = clean_h[:100] + "..."
        print("   ", clean_h)
