import subprocess, json, os

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
html = """<!DOCTYPE html><html><head><link rel="stylesheet" href="styles.css"></head><body>
<div style="width: 1000px;">
  <span id="s1" class="work-speaks-title" style="white-space: nowrap; display: inline-block; text-transform: none !important;">The work</span>
  <span id="s2" class="work-speaks-title" style="white-space: nowrap; display: inline-block;">THE WORK</span>
  <span id="s3" class="work-speaks-title" style="white-space: nowrap; display: inline-block;"><em>speaks</em></span>
  <span id="s4" class="work-speaks-title" style="white-space: nowrap; display: inline-block;"><em>SPEAKS</em></span>
</div>
<script>
window.addEventListener("load", () => {
  document.title = "WIDTHS:" + JSON.stringify({
    s1: document.getElementById("s1").getBoundingClientRect().width,
    s2: document.getElementById("s2").getBoundingClientRect().width,
    s3: document.getElementById("s3").getBoundingClientRect().width,
    s4: document.getElementById("s4").getBoundingClientRect().width,
    intro_col: document.querySelector(".work-speaks-intro") ? document.querySelector(".work-speaks-intro").getBoundingClientRect().width : null
  });
});
</script></body></html>"""

with open("test_w.html", "w") as f:
    f.write(html)
res = subprocess.run([chrome_path, "--headless=new", "--disable-gpu", "--no-sandbox", "--allow-file-access-from-files", "--dump-dom", "--window-size=1440,900", "file:///" + os.path.abspath("test_w.html").replace("\\", "/")], capture_output=True, text=True, encoding='utf-8')
print("STDOUT length:", len(res.stdout))
for l in res.stdout.splitlines():
    if "<title>" in l:
        print("TITLE:", l)
if os.path.exists("test_w.html"):
    os.remove("test_w.html")
