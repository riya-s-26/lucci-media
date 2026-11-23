import os, re

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

for s_name, p, css_name in pages:
    print(f"\n=================== {s_name}: {p} ({css_name}) ===================")
    p_path = os.path.join(base, p)
    if os.path.exists(p_path):
        with open(p_path, 'r', encoding='utf-8') as f:
            html = f.read()
        headings = re.findall(r'(<(?:h1|h2|h3|h4|h5|h6)[^>]*>.*?</(?:h1|h2|h3|h4|h5|h6)>)', html, re.DOTALL | re.IGNORECASE)
        for h in headings:
            clean = ' '.join(h.split())
            print("  HTML heading:", clean)
    else:
        print("  HTML not found!")

    css_path = os.path.join(base, css_name)
    if os.path.exists(css_path):
        with open(css_path, 'r', encoding='utf-8') as f:
            css = f.read()
        # Find all font-family declarations in this css
        ffs = re.findall(r'([^{}]*\{[^{}]*font-family:[^{}]*\})', css, re.DOTALL)
        print(f"  --- CSS rules with font-family in {css_name} ---")
        for rule in ffs:
            clean_rule = ' '.join(rule.split())
            print("   ", clean_rule)
