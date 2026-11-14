import subprocess, os
from PIL import Image

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

html = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<link rel="stylesheet" href="styles.css">
<style>
body {
  background: #F4F3EF;
  font-family: Montserrat, sans-serif;
  padding: 40px;
}
.test-row {
  display: flex;
  align-items: center;
  gap: 24px;
  margin-bottom: 24px;
  padding: 16px;
  background: #FFF;
  border-radius: 8px;
}
.test-label {
  width: 140px;
  font-size: 13px;
  font-weight: 700;
  color: #333;
}
.opt {
  display: inline-flex;
  align-items: center;
}
.svg-arrow-1 {
  width: 0.78em;
  height: 0.78em;
  stroke: currentColor;
  stroke-width: 1.5;
  stroke-linecap: round;
  stroke-linejoin: round;
  display: inline-block;
  vertical-align: 0.05em;
  margin-left: 0.35em;
  flex-shrink: 0;
}
.svg-arrow-2 {
  width: 0.82em;
  height: 0.82em;
  stroke: currentColor;
  stroke-width: 1.4;
  stroke-linecap: round;
  stroke-linejoin: round;
  display: inline-block;
  vertical-align: 0.05em;
  margin-left: 0.35em;
  flex-shrink: 0;
}
.svg-arrow-3 {
  width: 0.85em;
  height: 0.85em;
  stroke: currentColor;
  stroke-width: 1.35;
  stroke-linecap: round;
  stroke-linejoin: round;
  display: inline-block;
  vertical-align: 0.05em;
  margin-left: 0.35em;
  flex-shrink: 0;
}
</style>
</head>
<body>

<h3>Comparison: Original Glyph vs SVG Options</h3>

<!-- Header CTA Button -->
<div class="test-row">
  <div class="test-label">Header CTA:</div>
  <div>Original: <a class="header-cta" href="#">Apply to work with us <span>↗</span></a></div>
  <div>Option 1: <a class="header-cta" href="#">Apply to work with us <span class="opt"><svg class="svg-arrow-1" viewBox="0 0 10 10" fill="none"><path d="M1.5 8.5L8.5 1.5M8.5 1.5H3.5M8.5 1.5V6.5"/></svg></span></a></div>
  <div>Option 2: <a class="header-cta" href="#">Apply to work with us <span class="opt"><svg class="svg-arrow-2" viewBox="0 0 11 11" fill="none"><path d="M2 9L9 2M9 2H3.5M9 2V7.5"/></svg></span></a></div>
  <div>Option 3: <a class="header-cta" href="#">Apply to work with us <span class="opt"><svg class="svg-arrow-3" viewBox="0 0 12 12" fill="none"><path d="M2.5 9.5L9.5 2.5M9.5 2.5H4M9.5 2.5V8"/></svg></span></a></div>
</div>

<!-- Hero Button Light -->
<div class="test-row" style="background: #231E1B; color: #fff;">
  <div class="test-label" style="color: #fff;">Hero Button Light:</div>
  <div>Original: <a class="button button-light" href="#">Work with us <span>↗</span></a></div>
  <div>Option 1: <a class="button button-light" href="#">Work with us <span class="opt"><svg class="svg-arrow-1" viewBox="0 0 10 10" fill="none"><path d="M1.5 8.5L8.5 1.5M8.5 1.5H3.5M8.5 1.5V6.5"/></svg></span></a></div>
  <div>Option 2: <a class="button button-light" href="#">Work with us <span class="opt"><svg class="svg-arrow-2" viewBox="0 0 11 11" fill="none"><path d="M2 9L9 2M9 2H3.5M9 2V7.5"/></svg></span></a></div>
  <div>Option 3: <a class="button button-light" href="#">Work with us <span class="opt"><svg class="svg-arrow-3" viewBox="0 0 12 12" fill="none"><path d="M2.5 9.5L9.5 2.5M9.5 2.5H4M9.5 2.5V8"/></svg></span></a></div>
</div>

<!-- Archive Work Button -->
<div class="test-row">
  <div class="test-label">Archive Btn:</div>
  <div>Original: <a href="#" class="archive-work-btn">VIEW SERVICES ↗</a></div>
  <div>Option 1: <a href="#" class="archive-work-btn">VIEW SERVICES <span class="opt"><svg class="svg-arrow-1" viewBox="0 0 10 10" fill="none"><path d="M1.5 8.5L8.5 1.5M8.5 1.5H3.5M8.5 1.5V6.5"/></svg></span></a></div>
  <div>Option 2: <a href="#" class="archive-work-btn">VIEW SERVICES <span class="opt"><svg class="svg-arrow-2" viewBox="0 0 11 11" fill="none"><path d="M2 9L9 2M9 2H3.5M9 2V7.5"/></svg></span></a></div>
  <div>Option 3: <a href="#" class="archive-work-btn">VIEW SERVICES <span class="opt"><svg class="svg-arrow-3" viewBox="0 0 12 12" fill="none"><path d="M2.5 9.5L9.5 2.5M9.5 2.5H4M9.5 2.5V8"/></svg></span></a></div>
</div>

<!-- Text Link -->
<div class="test-row">
  <div class="test-label">Text Link:</div>
  <div>Original: <a class="text-link" href="#">APPLY TO WORK TOGETHER <span>↗</span></a></div>
  <div>Option 1: <a class="text-link" href="#">APPLY TO WORK TOGETHER <span class="opt"><svg class="svg-arrow-1" viewBox="0 0 10 10" fill="none"><path d="M1.5 8.5L8.5 1.5M8.5 1.5H3.5M8.5 1.5V6.5"/></svg></span></a></div>
  <div>Option 2: <a class="text-link" href="#">APPLY TO WORK TOGETHER <span class="opt"><svg class="svg-arrow-2" viewBox="0 0 11 11" fill="none"><path d="M2 9L9 2M9 2H3.5M9 2V7.5"/></svg></span></a></div>
  <div>Option 3: <a class="text-link" href="#">APPLY TO WORK TOGETHER <span class="opt"><svg class="svg-arrow-3" viewBox="0 0 12 12" fill="none"><path d="M2.5 9.5L9.5 2.5M9.5 2.5H4M9.5 2.5V8"/></svg></span></a></div>
</div>

<!-- TSA Banner Link -->
<div class="test-row" style="background: #1E1B18; color: #fff;">
  <div class="test-label" style="color: #fff;">TSA Banner Link:</div>
  <div>Original: <a href="#" class="tsa-cta-banner-link"><span>WORK WITH US</span> <span class="tsa-cta-arrow">↗</span></a></div>
  <div>Option 1: <a href="#" class="tsa-cta-banner-link"><span>WORK WITH US</span> <span class="tsa-cta-arrow opt"><svg class="svg-arrow-1" viewBox="0 0 10 10" fill="none"><path d="M1.5 8.5L8.5 1.5M8.5 1.5H3.5M8.5 1.5V6.5"/></svg></span></a></div>
  <div>Option 2: <a href="#" class="tsa-cta-banner-link"><span>WORK WITH US</span> <span class="tsa-cta-arrow opt"><svg class="svg-arrow-2" viewBox="0 0 11 11" fill="none"><path d="M2 9L9 2M9 2H3.5M9 2V7.5"/></svg></span></a></div>
  <div>Option 3: <a href="#" class="tsa-cta-banner-link"><span>WORK WITH US</span> <span class="tsa-cta-arrow opt"><svg class="svg-arrow-3" viewBox="0 0 12 12" fill="none"><path d="M2.5 9.5L9.5 2.5M9.5 2.5H4M9.5 2.5V8"/></svg></span></a></div>
</div>

<!-- Mobile Contact Pill -->
<div class="test-row">
  <div class="test-label">Mobile Contact:</div>
  <div style="width: 200px;">Original: <a class="mobile-contact" href="#" style="background: #2D1118; color: #fff; padding: 12px 16px; border-radius: 999px; display: flex; justify-content: space-between; font-size: 11px; text-decoration: none;">Apply to work with us <span>↗</span></a></div>
  <div style="width: 200px;">Option 2: <a class="mobile-contact" href="#" style="background: #2D1118; color: #fff; padding: 12px 16px; border-radius: 999px; display: flex; justify-content: space-between; font-size: 11px; text-decoration: none;">Apply to work with us <span class="opt"><svg class="svg-arrow-2" viewBox="0 0 11 11" fill="none"><path d="M2 9L9 2M9 2H3.5M9 2V7.5"/></svg></span></a></div>
</div>

</body>
</html>
"""

test_path = os.path.abspath('scratch/test_arrows_page.html')
with open(test_path, 'w', encoding='utf-8') as f:
    f.write(html)

shot = os.path.abspath('scratch/test_arrows_render.png')
cmd = [
    chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
    '--allow-file-access-from-files',
    '--window-size=1200,1000',
    f'--screenshot={shot}',
    'file:///' + test_path.replace('\\', '/')
]
subprocess.run(cmd, capture_output=True)
print("Saved scratch/test_arrows_render.png")

