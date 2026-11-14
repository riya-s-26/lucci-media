import subprocess, os, json
from PIL import Image

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
os.makedirs('review', exist_ok=True)

# SVG markup
svg_code = '<svg class="cta-arrow-icon" viewBox="0 0 10 10" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M1.5 8.5L8.5 1.5M8.5 1.5H3.5M8.5 1.5V6.5" stroke="currentColor" stroke-width="1.35" stroke-linecap="round" stroke-linejoin="round"/></svg>'

# Test page generator
def create_test_page(source_html):
    with open(source_html, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace('<span aria-hidden="true">↗</span>', f'<span aria-hidden="true">{svg_code}</span>')
    c = c.replace('<span>↗</span>', f'<span>{svg_code}</span>')
    c = c.replace('VIEW SERVICES ↗', f'VIEW SERVICES <span class="cta-arrow-inline" aria-hidden="true">{svg_code}</span>')
    c = c.replace('ABOUT LUCCI MEDIA ↗', f'ABOUT LUCCI MEDIA <span class="cta-arrow-inline" aria-hidden="true">{svg_code}</span>')
    return c

css_rules = """
/* MONOCHROME CTA EXTERNAL ARROW ICON SYSTEM */
.cta-arrow-icon {
  width: 0.78em;
  height: 0.78em;
  display: inline-block;
  vertical-align: 0.04em;
  flex-shrink: 0;
  stroke: currentColor;
  stroke-width: 1.35;
  stroke-linecap: round;
  stroke-linejoin: round;
  fill: none;
}

.header-cta span,
.button span,
.text-link span,
.archive-work-btn span,
.cs-btn-secondary span,
.about-cta-button span,
.about-text-link span {
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.archive-work-btn .cta-arrow-inline,
.cs-btn-secondary .cta-arrow-inline {
  display: inline-flex;
  align-items: center;
  margin-left: 0.4em;
}

.mobile-menu .mobile-contact span {
  display: inline-flex;
  align-items: center;
}

.mobile-menu .mobile-contact .cta-arrow-icon {
  width: 0.85em;
  height: 0.85em;
}

.tsa-cta-banner-link .tsa-cta-arrow {
  display: inline-flex;
  align-items: center;
}

.tsa-cta-banner-link .tsa-cta-arrow .cta-arrow-icon {
  width: 0.85em;
  height: 0.85em;
}
"""

with open('scratch/button_showcase.html', 'w', encoding='utf-8') as f:
    f.write(f"""<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="../styles.css">
<style>
{css_rules}
body {{
  background: #FAF9F6;
  font-family: Montserrat, sans-serif;
  padding: 30px;
}}
.card {{
  background: #FFFFFF;
  border: 1px solid #E5E5E3;
  padding: 20px 24px;
  margin-bottom: 20px;
  border-radius: 6px;
}}
.card-title {{
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.14em;
  color: #8A847F;
  margin-bottom: 14px;
  text-transform: uppercase;
}}
.dark-wrap {{
  background: #1E1B18;
  padding: 24px;
  border-radius: 6px;
}}
</style>
</head>
<body>

<div class="card">
  <div class="card-title">1. Site Header CTA (.header-cta)</div>
  <a class="header-cta" href="#" style="display:inline-flex;">Apply to work with us <span aria-hidden="true">{svg_code}</span></a>
</div>

<div class="card">
  <div class="card-title">2. Hero Action Button (.button .button-light)</div>
  <div class="dark-wrap">
    <a class="button button-light" href="#" style="display:inline-flex;">Work with us <span aria-hidden="true">{svg_code}</span></a>
  </div>
</div>

<div class="card">
  <div class="card-title">3. Archive Work Button (.archive-work-btn)</div>
  <div style="background: #FFF; padding: 10px;">
    <a href="#" class="archive-work-btn">VIEW SERVICES <span class="cta-arrow-inline" aria-hidden="true">{svg_code}</span></a>
  </div>
</div>

<div class="card">
  <div class="card-title">4. Text Link (.text-link)</div>
  <a class="text-link" href="#">APPLY TO WORK TOGETHER <span aria-hidden="true">{svg_code}</span></a>
</div>

<div class="card">
  <div class="card-title">5. TSA Editorial Banner Action (.tsa-cta-banner-link)</div>
  <div class="dark-wrap">
    <a href="#" class="tsa-cta-banner-link">
      <span>WORK WITH US</span>
      <span class="tsa-cta-arrow" aria-hidden="true">{svg_code}</span>
    </a>
  </div>
</div>

<div class="card">
  <div class="card-title">6. Mobile Contact Pill (.mobile-contact)</div>
  <div style="max-width: 320px;">
    <a class="mobile-contact" href="#" style="display:flex; justify-content:space-between; align-items:center; background:#2D1118; color:#fff; padding:15px 18px; border-radius:999px; font-size:11px; font-weight:700; text-decoration:none; letter-spacing:0.12em;">
      APPLY TO WORK WITH US <span>{svg_code}</span>
    </a>
  </div>
</div>

<div class="card">
  <div class="card-title">7. Coming Soon Action Button (.cs-btn-secondary)</div>
  <a href="#" class="cs-btn cs-btn-secondary" style="display:inline-flex; align-items:center; justify-content:center; padding:12px 24px; font-size:11px; font-weight:700; letter-spacing:0.1em; text-decoration:none; border:1px solid #1E1B18; color:#1E1B18;">
    ABOUT LUCCI MEDIA <span class="cta-arrow-inline" aria-hidden="true">{svg_code}</span>
  </a>
</div>

<div class="card">
  <div class="card-title">8. Footer Social Link (.footer-meta-left a)</div>
  <a href="#" style="font-family: var(--label); font-size: 10px; font-weight: 700; letter-spacing: 0.12em; color: #1E1B18; text-decoration: none; text-transform: uppercase;">
    CONNECT ON IG + TIKTOK <span aria-hidden="true">{svg_code}</span>
  </a>
</div>

</body>
</html>""")

# Render showcase across viewports
for name, w in [('desktop', 1000), ('ipad', 768), ('iphone', 375)]:
    shot = os.path.abspath(f'review/showcase_{name}.png')
    cmd = [
        chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
        '--allow-file-access-from-files',
        f'--window-size={w},1600',
        f'--screenshot={shot}',
        'file:///' + os.path.abspath('scratch/button_showcase.html').replace('\\', '/')
    ]
    subprocess.run(cmd, capture_output=True)
    print(f'Rendered showcase for {name}')

print("Showcase rendering complete.")

