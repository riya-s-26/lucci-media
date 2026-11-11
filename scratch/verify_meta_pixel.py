import subprocess
import os
import json

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

pages = [
    'index.html',
    'about.html',
    'coming-soon.html',
    'services.html',
    'the-work.html',
    'our-studio.html',
    'inquire.html'
]

print("=== VERIFYING META PIXEL CODE PRESENCE IN HTML FILES ===")
pixel_id = "1985395006178197"
all_passed = True

for page in pages:
    with open(page, 'r', encoding='utf-8') as f:
        html = f.read()
        
    has_script = "https://connect.facebook.net/en_US/fbevents.js" in html
    has_init = f"fbq('init', '{pixel_id}')" in html
    has_track = "fbq('track', 'PageView')" in html
    has_noscript = f"https://www.facebook.com/tr?id={pixel_id}&ev=PageView&noscript=1" in html
    init_count = html.count("fbq('init'")
    
    print(f"File: {page:18} | Script: {has_script} | Init: {has_init} | Track: {has_track} | Noscript: {has_noscript} | Init Count: {init_count}")
    if not (has_script and has_init and has_track and has_noscript and init_count == 1):
        all_passed = False

print(f"\nAll static file checks passed? {all_passed}")

print("\n=== RUNNING BROWSER EXECUTION TESTS IN HEADLESS CHROME ===")

# For the 3 core rendered pages: index.html, about.html, coming-soon.html
# We test in Chrome by dumping DOM with verification script
core_pages = ['index.html', 'about.html', 'coming-soon.html']

for page in core_pages:
    url = f"file:///{os.path.abspath(page).replace(os.sep, '/')}"
    
    # We create a temporary test wrapper that runs right after fbq is defined to inspect queue and state
    with open(page, 'r', encoding='utf-8') as f:
        html = f.read()
        
    test_verify_script = """
    <script>
    window.addEventListener('DOMContentLoaded', () => {
        const q = window.fbq && window.fbq.queue ? Array.from(window.fbq.queue).map(a => Array.from(a)) : [];
        const inits = q.filter(item => item[0] === 'init');
        const tracks = q.filter(item => item[0] === 'track' && item[1] === 'PageView');
        const noscript = document.querySelector('noscript');
        const result = {
            fbqExists: typeof window.fbq === 'function',
            fbqVersion: window.fbq ? window.fbq.version : null,
            initCount: inits.length,
            initId: inits.length > 0 ? inits[0][1] : null,
            pageViewTracked: tracks.length === 1,
            queueLength: q.length,
            queue: q
        };
        document.title = 'TEST_RESULT_' + JSON.stringify(result);
    });
    </script>
    """
    temp_file = os.path.abspath(f"temp_pixel_test_{page}")
    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write(html.replace('</body>', test_verify_script + '</body>'))
        
    cmd = [
        chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
        '--allow-file-access-from-files',
        f'file:///{temp_file.replace(os.sep, "/")}',
        '--dump-dom'
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    for line in res.stdout.splitlines():
        if '<title>TEST_RESULT_' in line:
            json_str = line.split('<title>TEST_RESULT_')[1].split('</title>')[0]
            data = json.loads(json_str)
            print(f"\nPage: {page}")
            print(f"  - window.fbq initialized: {data['fbqExists']}")
            print(f"  - Pixel version: {data['fbqVersion']}")
            print(f"  - Correct Pixel ID initialized: {data['initId']} (Expected: {pixel_id})")
            print(f"  - Initialization count: {data['initCount']} (Expected: 1)")
            print(f"  - PageView event queued/triggered: {data['pageViewTracked']}")
            print(f"  - Complete Queue: {data['queue']}")
            
    if os.path.exists(temp_file):
        os.remove(temp_file)

