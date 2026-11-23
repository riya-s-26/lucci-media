import os
import subprocess

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(edge_path):
    edge_path = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"

html_file = os.path.abspath(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\med-spa-website-design.html")
file_url = f"file:///{html_file.replace(os.sep, '/')}"
out_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch"
temp_profile = os.path.join(out_dir, "edge_profile")

# We can capture a large window height e.g. 1440x2600 to capture the whole page!
out_full = os.path.join(out_dir, "render_web_full.png")
cmd = [
    edge_path,
    "--headless",
    "--disable-gpu",
    "--no-sandbox",
    f"--user-data-dir={temp_profile}",
    "--window-size=1440,2800",
    f"--screenshot={out_full}",
    file_url
]

res = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
if os.path.exists(out_full):
    print("Full page screenshot success:", os.path.getsize(out_full), "bytes")
else:
    print("Full page screenshot failed:", res.stderr)
