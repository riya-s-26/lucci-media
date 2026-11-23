import os
import subprocess

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(edge_path):
    edge_path = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"

html_file = os.path.abspath(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\med-spa-website-design.html")
file_url = f"file:///{html_file.replace(os.sep, '/')}"
out_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch"

viewports = [
    ("desktop", 1440, 900),
    ("tablet", 1024, 768),
    ("mobile", 390, 844)
]

for name, w, h in viewports:
    out_img = os.path.join(out_dir, f"render_web_{name}.png")
    cmd = [
        edge_path,
        "--headless=new",
        f"--window-size={w},{h}",
        f"--screenshot={out_img}",
        "--hide-scrollbars",
        file_url
    ]
    print(f"Capturing {name} screenshot ({w}x{h})...")
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=20)
    if os.path.exists(out_img):
        print(f"  Saved {name} screenshot: {os.path.getsize(out_img)} bytes")
    else:
        print(f"  Failed for {name}: {res.stderr}")

print("Screenshot capture complete!")
