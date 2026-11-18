import subprocess, json, time, urllib.request

proc = subprocess.Popen([
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    '--headless=new',
    '--no-sandbox',
    '--disable-gpu',
    '--remote-debugging-port=9222',
    '--window-size=390,844',
    'file:///c:/xampp/htdocs/luci/inquire.html'
])

time.sleep(1.5)

try:
    tabs = json.loads(urllib.request.urlopen('http://localhost:9222/json').read())
    ws_url = tabs[0]['webSocketDebuggerUrl']
    print("Connected to:", ws_url)
finally:
    proc.terminate()
