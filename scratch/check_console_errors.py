import subprocess
import os
import json

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
core_pages = ['index.html', 'about.html', 'coming-soon.html']

for page in core_pages:
    with open(page, 'r', encoding='utf-8') as f:
        html = f.read()
        
    error_collector = """
    <script>
    window.__pageErrors = [];
    window.addEventListener('error', (e) => {
        window.__pageErrors.push({message: e.message, filename: e.filename, lineno: e.lineno});
    });
    </script>
    """
    error_checker = """
    <script>
    window.addEventListener('DOMContentLoaded', () => {
        document.title = 'CONSOLE_ERRORS_' + JSON.stringify(window.__pageErrors);
    });
    </script>
    """
    temp_file = os.path.abspath(f"temp_err_test_{page}")
    with open(temp_file, 'w', encoding='utf-8') as f:
        # insert error collector at start of head and checker before end of body
        content = html.replace('<head>', '<head>' + error_collector)
        content = content.replace('</body>', error_checker + '</body>')
        f.write(content)
        
    cmd = [
        chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
        '--allow-file-access-from-files',
        f'file:///{temp_file.replace(os.sep, "/")}',
        '--dump-dom'
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    for line in res.stdout.splitlines():
        if '<title>CONSOLE_ERRORS_' in line:
            json_str = line.split('<title>CONSOLE_ERRORS_')[1].split('</title>')[0]
            errs = json.loads(json_str)
            print(f"Page: {page:16} | JavaScript execution errors: {len(errs)} | Details: {errs}")
            
    if os.path.exists(temp_file):
        os.remove(temp_file)
