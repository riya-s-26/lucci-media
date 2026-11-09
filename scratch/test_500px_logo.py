import subprocess
import os

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

for w in [1440, 1920]:
    print(f"\n=== Testing Viewport {w}px ===")
    for page in ['about.html', 'index.html', 'coming-soon.html']:
        script_code = f"""
        <script>
        window.addEventListener('load', () => {{
            const el = document.querySelector('.footer-brand-logo');
            if (el) {{
                const r = el.getBoundingClientRect();
                const cs = window.getComputedStyle(el);
                document.title = 'MEASURE_' + Math.round(r.width) + 'x' + Math.round(r.height) + '_computed:' + cs.width + 'x' + cs.height;
            }}
        }});
        </script>
        """
        with open(page, 'r', encoding='utf-8') as f:
            html = f.read()
            
        test_path = os.path.abspath(f'temp_test_500_{page}')
        with open(test_path, 'w', encoding='utf-8') as f:
            f.write(html.replace('</body>', script_code + '</body>'))
            
        test_url = 'file:///' + test_path.replace(os.sep, '/')
        cmd = [
            chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
            '--allow-file-access-from-files', f'--window-size={w},2000',
            '--dump-dom', test_url
        ]
        res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
        for line in res.stdout.splitlines():
            if '<title>MEASURE_' in line:
                print(f"{page} @ {w}px: {line.strip()}")
                
        if os.path.exists(test_path):
            os.remove(test_path)
