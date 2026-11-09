import subprocess

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
file_url = "file:///C:/xampp/htdocs/luci/about.html"

# Run chrome headless with --dump-dom or evaluate script
js_script = "console.log('DOC_HEIGHT:' + document.documentElement.scrollHeight);"
cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--allow-file-access-from-files",
    "--window-size=390,844",
    f"--run-all-compositor-stages-before-draw",
    f"--virtual-time-budget=2000",
    f"--dump-dom",
    file_url
]
# Wait, let's write a python script that launches chrome with remote-debugging-port to get exact scrollHeight via CDP

