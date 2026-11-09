import subprocess
import os

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

widths = [1440, 768, 390, 320]

for w in widths:
    print(f"\n--- Testing Viewport Width: {w}px ---")
    for page in ['about.html', 'index.html', 'coming-soon.html']:
        with open(page, 'r', encoding='utf-8') as f:
            html = f.read()
        
        script_code = f"""
        <script>
        window.addEventListener('load', () => {{
            const el = document.querySelector('.footer-brand-logo');
            if (el) {{
                const r = el.getBoundingClientRect();
                document.title = 'RECT_' + Math.round(r.width) + 'x' + Math.round(r.height);
            }}
        }});
        </script>
        """
        test_html = html.replace('</body>', script_code + '</body>')
        test_path = os.path.abspath(f'temp_test_{page}')
        with open(test_path, 'w', encoding='utf-8') as f:
            f.write(test_html)
            
        cmd = [
            chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
            '--allow-file-access-from-files',
            f'--window-size={w},2000',
            '--dump-dom',
            f'file:///{test_path.replace(os.sep, "/")}'
        ]
        res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
        for line in res.stdout.splitlines():
            if '<title>RECT_' in line:
                print(f"{page} ({w}px): {line.strip()}")
                
        if os.path.exists(test_path):
            os.remove(test_path)
