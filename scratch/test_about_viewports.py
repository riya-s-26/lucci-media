import subprocess
import os
from PIL import Image

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

with open('about.css', 'r', encoding='utf-8') as f:
    orig_css = f.read()

spacing_options = [
    ('ls_default', 'letter-spacing: 0.02em;'),
    ('ls_wwdb', 'letter-spacing: 0.08em;'),
    ('ls_tight', 'letter-spacing: -0.01em;'),
    ('ls_orig', 'letter-spacing: -0.025em;')
]

viewports = [
    ('1440', 1440, 1000),
    ('1024', 1024, 1000),
    ('768', 768, 1000),
    ('390', 390, 900)
]

for s_label, s_rule in spacing_options:
    test_rule = f"""
.about-hero-title {{
  margin: 0 0 24px 0;
  font-family: 'ShapiroWideRegular', 'Montserrat', var(--sans);
  font-style: normal;
  font-size: clamp(38px, 4.2vw, 56px);
  font-weight: 700;
  line-height: 1.05;
  {s_rule}
  color: var(--about-text-dark);
  text-transform: uppercase !important;
}}
"""
    mod_css = orig_css.replace("""
.about-hero-title {
  margin: 0 0 24px 0;
  font-family: var(--sans);
  font-style: italic;
  font-size: clamp(38px, 4.2vw, 56px);
  font-weight: 800;
  line-height: 1.05;
  letter-spacing: -0.025em;
  color: var(--about-text-dark);
  text-transform: uppercase !important;
}
""".strip(), test_rule.strip())

    with open('about.css', 'w', encoding='utf-8') as f:
        f.write(mod_css)
        
    for vp_label, w, h in viewports:
        shot = os.path.abspath(f'scratch/vp_{s_label}_{vp_label}.png')
        cmd = [
            chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
            '--allow-file-access-from-files', '--hide-scrollbars',
            '--force-prefers-reduced-motion',
            f'--window-size={w},{h}', f'--screenshot={shot}',
            'file:///C:/xampp/htdocs/luci/about.html'
        ]
        subprocess.run(cmd, check=True)
        im = Image.open(shot)
        crop = im.crop((0, 100, min(w, 800), 700))
        crop.save(f'scratch/crop_{s_label}_{vp_label}.png')
        if os.path.exists(shot):
            os.remove(shot)

# Restore about.css
with open('about.css', 'w', encoding='utf-8') as f:
    f.write(orig_css)

print('Done rendering all spacing options across viewports')

