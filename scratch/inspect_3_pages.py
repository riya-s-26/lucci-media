import re

pages = [
    'beauty-campaign-production.html',
    'beauty-brand-identity-design.html',
    'med-spa-website-design.html'
]

for p in pages:
    print(f"\n==================== {p} ====================")
    with open(p, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find stylesheets
    css_files = re.findall(r'<link[^>]+href=["\']([^"\']+\.css[^"\']*)["\']', html)
    print("Stylesheets:", css_files)

    # Find img tags
    img_tags = re.findall(r'<img[^>]+>', html)
    for tag in img_tags:
        src_m = re.search(r'src=["\']([^"\']+)["\']', tag)
        alt_m = re.search(r'alt=["\']([^"\']*)["\']', tag)
        src = src_m.group(1) if src_m else ''
        alt = alt_m.group(1) if alt_m else ''
        if not any(k in src.lower() for k in ['logo', 'favicon', 'icon', 'svg']):
            print(f"  [IMG] src='{src}' alt='{alt}'")

    # Check background images in linked CSS
    for css in css_files:
        css_clean = css.split('?')[0]
        try:
            with open(css_clean, 'r', encoding='utf-8') as cf:
                css_text = cf.read()
                bg_imgs = re.findall(r'url\([\'"]?([^\'")]+)[\'"]?\)', css_text)
                for bg in bg_imgs:
                    if not any(k in bg.lower() for k in ['font', 'woff', 'ttf', 'otf', 'svg']):
                        print(f"  [CSS BG in {css_clean}] {bg}")
        except Exception as e:
            pass
