import os, re
from bs4 import BeautifulSoup

base = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media"

pages = [
  ('Service 1', 'social-media-management-boston.html', 'service-page.css'),
  ('Service 2', 'beauty-content-creation-boston.html', 'trending-socials.css'),
  ('Service 3', 'brand-photography-boston.html', 'brand-photography.css'),
  ('Service 4', 'beauty-campaign-production.html', 'campaign-shoots.css'),
  ('Service 5', 'beauty-brand-identity-design.html', 'brand-identity.css'),
  ('Service 6', 'med-spa-website-design.html', 'website-design.css'),
  ('Service 7', 'google-business-profile-management.html', 'google-business-profile.css'),
  ('Service 8', 'local-seo-med-spas.html', 'coming-soon.css')
]

for s_num, html_file, css_file in pages:
    print(f"\n================ {s_num}: {html_file} ({css_file}) ================")
    css_path = os.path.join(base, css_file)
    with open(css_path, 'r', encoding='utf-8') as f:
        css_text = f.read()
    
    html_path = os.path.join(base, html_file)
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    main = soup.find('main')
    if not main:
        main = soup.find('body')
    
    headings = main.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    for h in headings:
        # find matching class rules
        classes = h.get('class', [])
        tag = h.name
        hid = h.get('id', '')
        
        # search css for tag, classes, id
        found_rules = []
        for c in classes:
            m = re.findall(rf'(\.{c}[^{{}}]*\{{[^{{}}]*font-family:[^;}}]+[;}}])', css_text)
            found_rules.extend(m)
        if hid:
            m = re.findall(rf'(#{hid}[^{{}}]*\{{[^{{}}]*font-family:[^;}}]+[;}}])', css_text)
            found_rules.extend(m)
        m = re.findall(rf'([^{{}}]*\b{tag}\b[^{{}}]*\{{[^{{}}]*font-family:[^;}}]+[;}}])', css_text)
        found_rules.extend(m)
        
        print(f"  <{tag} class='{' '.join(classes)}' id='{hid}'>: '{' '.join(h.get_text().split())[:50]}'")
        if found_rules:
            for r in set(found_rules):
                print(f"     RULE: {' '.join(r.split())}")
        else:
            print("     NO DIRECT RULE (inherited)")
