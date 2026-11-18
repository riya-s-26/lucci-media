import subprocess, os

html = open(r'c:\xampp\htdocs\luci\inquire.html', 'r', encoding='utf-8').read()
html = html.replace('id="inquiry-form" class="inquiry-form"', 'id="inquiry-form" class="inquiry-form" style="display:none"')
html = html.replace('id="inquiry-confirmation" class="inquiry-confirmation" hidden', 'id="inquiry-confirmation" class="inquiry-confirmation"')

with open(r'c:\xampp\htdocs\luci\test-confirmation.html', 'w', encoding='utf-8') as f:
    f.write(html)

subprocess.run([
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    '--headless=new',
    '--no-sandbox',
    '--disable-gpu',
    '--window-size=390,1300',
    r'--screenshot=c:\xampp\htdocs\luci\screenshot-confirmation-mobile-full.png',
    'file:///c:/xampp/htdocs/luci/test-confirmation.html'
], check=True)

if os.path.exists(r'c:\xampp\htdocs\luci\test-confirmation.html'):
    os.remove(r'c:\xampp\htdocs\luci\test-confirmation.html')

print("Full mobile confirmation done.")
