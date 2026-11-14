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
  background: #FAF9F6;
  font-family: Montserrat, sans-serif;
  padding: 40px;
}
.test-section {
  background: #FFF;
  border: 1px solid #E5E5E3;
  padding: 24px;
  margin-bottom: 24px;
  border-radius: 8px;
}
h2 {
  font-size: 14px;
  font-weight: 700;
  color: #8A847F;
  margin-top: 0;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}
.row {
  display: flex;
  align-items: center;
  gap: 32px;
}
.col {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.label {
  font-size: 11px;
  font-weight: 600;
  color: #666;
}

/* Pause/Play SVGs */
.archive-pause-icon {
  width: 9px;
  height: 9px;
  display: inline-block;
  vertical-align: -0.05em;
  fill: currentColor;
  flex-shrink: 0;
}

/* Star SVG */
.sparkle-svg {
  width: 1em;
  height: 1em;
  display: inline-block;
  vertical-align: middle;
  stroke: currentColor;
  fill: none;
}
</style>
</head>
<body>

<div class="test-section">
  <h2>1. Star / Asterisk Icons</h2>
  <div class="row">
    <div class="col">
      <div class="label">Original Desktop Glyph (✳):</div>
      <div style="font-size: 32px; color: #2D1118;">✳</div>
    </div>
    <div class="col">
      <div class="label">SVG Star Option A (stroke 2, round):</div>
      <div style="font-size: 32px; color: #2D1118;">
        <svg class="sparkle-svg" viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round">
          <line x1="12" y1="2" x2="12" y2="22"/>
          <line x1="2" y1="12" x2="22" y2="12"/>
          <line x1="4.93" y1="4.93" x2="19.07" y2="19.07"/>
          <line x1="19.07" y1="4.93" x2="4.93" y2="19.07"/>
        </svg>
      </div>
    </div>
    <div class="col">
      <div class="label">SVG Star Option B (stroke 2.3, round):</div>
      <div style="font-size: 32px; color: #2D1118;">
        <svg class="sparkle-svg" viewBox="0 0 24 24" stroke-width="2.3" stroke-linecap="round">
          <line x1="12" y1="2" x2="12" y2="22"/>
          <line x1="2" y1="12" x2="22" y2="12"/>
          <line x1="4.93" y1="4.93" x2="19.07" y2="19.07"/>
          <line x1="19.07" y1="4.93" x2="4.93" y2="19.07"/>
        </svg>
      </div>
    </div>
    <div class="col">
      <div class="label">Large Flower (Contact Section, 67px, 8% black):</div>
      <div style="font-size: 67px; color: rgba(0,0,0,0.08);">
        <svg class="sparkle-svg" viewBox="0 0 24 24" stroke-width="2.2" stroke-linecap="round">
          <line x1="12" y1="2" x2="12" y2="22"/>
          <line x1="2" y1="12" x2="22" y2="12"/>
          <line x1="4.93" y1="4.93" x2="19.07" y2="19.07"/>
          <line x1="19.07" y1="4.93" x2="4.93" y2="19.07"/>
        </svg>
      </div>
    </div>
  </div>
</div>

<div class="test-section">
  <h2>2. Archive Pause / Play Button</h2>
  <div class="row">
    <div class="col">
      <div class="label">Original Desktop Button (Pause):</div>
      <button class="archive-pause-toggle" type="button">
        <span class="pause-icon" aria-hidden="true">⏸</span>
        <span class="pause-text">Pause</span>
      </button>
    </div>
    <div class="col">
      <div class="label">SVG Pause Button:</div>
      <button class="archive-pause-toggle" type="button">
        <span class="pause-icon" aria-hidden="true">
          <svg class="archive-pause-icon" viewBox="0 0 10 10">
            <rect x="1.5" y="1" width="2.4" height="8" rx="0.5"/>
            <rect x="6.1" y="1" width="2.4" height="8" rx="0.5"/>
          </svg>
        </span>
        <span class="pause-text">Pause</span>
      </button>
    </div>
    <div class="col">
      <div class="label">SVG Play Button:</div>
      <button class="archive-pause-toggle" type="button" aria-pressed="true">
        <span class="pause-icon" aria-hidden="true">
          <svg class="archive-pause-icon" viewBox="0 0 10 10">
            <polygon points="2,1 8.5,5 2,9"/>
          </svg>
        </span>
        <span class="pause-text">Play</span>
      </button>
    </div>
  </div>
</div>

</body>
</html>
"""

test_path = os.path.abspath('scratch/test_prototype.html')
with open(test_path, 'w', encoding='utf-8') as f:
    f.write(html)

shot = os.path.abspath('scratch/test_prototype.png')
cmd = [
    chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
    '--allow-file-access-from-files',
    '--window-size=1200,800',
    f'--screenshot={shot}',
    'file:///' + test_path.replace('\\', '/')
]
subprocess.run(cmd, capture_output=True)
print("Saved scratch/test_prototype.png")

