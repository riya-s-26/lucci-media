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

print("=== AUDIT OF SERVICE HEADINGS FONT-FAMILY ===")

for s_num, html_file, css_file in pages:
    html_path = os.path.join(base, html_file)
    css_path = os.path.join(base, css_file)
    
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    with open(css_path, 'r', encoding='utf-8') as f:
        css = f.read()
    
    print(f"\n--- {s_num}: {html_file} ({css_file}) ---")
    
    main = soup.find('main')
    if not main:
        main = soup.find('body')
        
    headings = main.find_all(['h1', 'h2', 'h3'])
    for h in headings:
        classes = [c for c in h.get('class', []) if c]
        hid = h.get('id', '')
        tag = h.name
        text = ' '.join(h.get_text().split())[:60]
        
        # Check if inside FAQ
        in_faq = bool(
            h.find_parent(id=re.compile(r'faq', re.I)) or 
            h.find_parent(class_=re.compile(r'faq', re.I)) or
            'faq' in hid.lower() or
            any('faq' in c.lower() for c in classes)
        )
        
        # Determine applicable font-family
        matched_ff = None
        style_tags = soup.find_all('style')
        for st in style_tags:
            for c in classes:
                m = re.search(r'\.' + re.escape(c) + r'[^\{]*\{[^\}]*font-family:\s*([^;\}]+)', st.text)
                if m:
                    matched_ff = m.group(1).strip()
        
        if not matched_ff and classes:
            for c in classes:
                m = re.findall(r'\.' + re.escape(c) + r'[^\{]*\{[^\}]*font-family:\s*([^;\}]+)', css)
                if m:
                    matched_ff = m[-1].strip()
        
        if not matched_ff:
            # check parent classes
            parent = h.parent
            while parent and parent != main and not matched_ff:
                p_classes = [c for c in parent.get('class', []) if c]
                for pc in p_classes:
                    m = re.findall(r'\.' + re.escape(pc) + r'\s+' + tag + r'[^\{]*\{[^\}]*font-family:\s*([^;\}]+)', css)
                    if m:
                        matched_ff = m[-1].strip()
                parent = parent.parent
                
        # check CSS variables
        if matched_ff and 'var(--' in matched_ff:
            var_name = re.search(r'var\((--[^\,\)]+)', matched_ff).group(1)
            var_val = re.search(re.escape(var_name) + r':\s*([^;]+);', css)
            if var_val:
                matched_ff = f"{matched_ff} => {var_val.group(1).strip()}"
                
        faq_note = "[FAQ]" if in_faq else "[HEADING]"
        print(f"  {faq_note} <{tag} class='{' '.join(classes)}' id='{hid}'>: '{text}' => font: {matched_ff}")
