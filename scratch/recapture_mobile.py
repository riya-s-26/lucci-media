import subprocess
import os

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
file_url = "file:///C:/xampp/htdocs/luci/about.html"
mobile_out = os.path.abspath("review/mobile_about.png")

cmd_mobile = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--allow-file-access-from-files",
    "--hide-scrollbars",
    "--window-size=390,5400",
    f"--screenshot={mobile_out}",
    file_url
]
subprocess.run(cmd_mobile, check=True)
print("Mobile re-captured with 5400px height.")

