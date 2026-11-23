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
    path = os.path.join(base, html_file)
    with open(path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    # We ignore header, footer, mobile-menu because user said:
    # "Do not change paragraph fonts, FAQ text, homepage headings, shared header or footer."
    # Let's inspect headings inside main or outside header/footer:
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    print(f"\n================ {s_num}: {html_file} ================")
    for h in headings:
        # check if in header or footer
        in_header = bool(h.find_parent('header') or h.find_parent(class_=re.compile(r'header|mobile-menu')))
        in_footer = bool(h.find_parent('footer') or h.find_parent(class_=re.compile(r'footer')))
        if in_header:
            loc = "[HEADER]"
        elif in_footer:
            loc = "[FOOTER]"
        else:
            loc = "[CONTENT]"
        text = ' '.join(h.get_text().split())
        classes = h.get('class', [])
        hid = h.get('id', '')
        print(f"  {loc} <{h.name} class='{' '.join(classes)}' id='{hid}'>: {text[:80]}")
