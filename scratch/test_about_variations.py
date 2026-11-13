import subprocess
import os
from PIL import Image

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

# Read about.css
with open('about.css', 'r', encoding='utf-8') as f:
    orig_css = f.read()

tests = [
    # 1. Normal, font-weight 700 (matching WWDB)
    ('normal_700', """
.about-hero-title {
  margin: 0 0 24px 0;
  font-family: 'ShapiroWideRegular', 'Montserrat', var(--sans);
  font-style: normal;
  font-size: clamp(38px, 4.2vw, 56px);
  font-weight: 700;
  line-height: 1.05;
  letter-spacing: 0.02em;
  color: var(--about-text-dark);
  text-transform: uppercase !important;
}
"""),
    # 2. Normal, font-weight 400 (regular ShapiroWide)
    ('normal_400', """
.about-hero-title {
  margin: 0 0 24px 0;
  font-family: 'ShapiroWideRegular', 'Montserrat', var(--sans);
  font-style: normal;
  font-size: clamp(38px, 4.2vw, 56px);
  font-weight: 400;
  line-height: 1.05;
  letter-spacing: 0.02em;
  color: var(--about-text-dark);
  text-transform: uppercase !important;
}
"""),
    # 3. Normal, font-weight 700 with letter-spacing 0.08em (exact WWDB letter spacing)
    ('normal_700_wide', """
.about-hero-title {
  margin: 0 0 24px 0;
  font-family: 'ShapiroWideRegular', 'Montserrat', var(--sans);
  font-style: normal;
  font-size: clamp(38px, 4.2vw, 56px);
  font-weight: 700;
  line-height: 1.05;
  letter-spacing: 0.08em;
  color: var(--about-text-dark);
  text-transform: uppercase !important;
}
"""),
    # 4. Normal, keeping original letter-spacing -0.025em and font-weight 700
    ('normal_700_tight', """
.about-hero-title {
  margin: 0 0 24px 0;
  font-family: 'ShapiroWideRegular', 'Montserrat', var(--sans);
  font-style: normal;
  font-size: clamp(38px, 4.2vw, 56px);
  font-weight: 700;
  line-height: 1.05;
  letter-spacing: -0.025em;
  color: var(--about-text-dark);
  text-transform: uppercase !important;
}
"""),
    # 5. Italic, font-weight 700 (if italic was meant to be kept)
    ('italic_700', """
.about-hero-title {
  margin: 0 0 24px 0;
  font-family: 'ShapiroWideRegular', 'Montserrat', var(--sans);
  font-style: italic;
  font-size: clamp(38px, 4.2vw, 56px);
  font-weight: 700;
  line-height: 1.05;
  letter-spacing: -0.025em;
  color: var(--about-text-dark);
  text-transform: uppercase !important;
}
""")
]

target_rule = """
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
"""

for label, replacement in tests:
    mod_css = orig_css.replace(target_rule.strip(), replacement.strip())
    with open('about.css', 'w', encoding='utf-8') as f:
        f.write(mod_css)
        
    shot = os.path.abspath(f'scratch/about_test_{label}.png')
    cmd = [
        chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
        '--allow-file-access-from-files', '--hide-scrollbars',
        '--force-prefers-reduced-motion',
        '--window-size=1440,1100', f'--screenshot={shot}',
        'file:///C:/xampp/htdocs/luci/about.html'
    ]
    subprocess.run(cmd, check=True)
    im = Image.open(shot)
    crop = im.crop((0, 150, 750, 650))
    crop.save(f'scratch/crop_about_{label}.png')
    if os.path.exists(shot):
        os.remove(shot)

# Restore original about.css
with open('about.css', 'w', encoding='utf-8') as f:
    f.write(orig_css)

print('Done rendering about headline variations')

