import os
import glob
import re

base_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media"
html_files = glob.glob(os.path.join(base_dir, "**", "*.html"), recursive=True)

# 1. Update services.html row .06
services_html_path = os.path.join(base_dir, "services.html")
with open(services_html_path, 'r', encoding='utf-8') as f:
    s_content = f.read()

# Replace row .06 in services.html
old_row_06 = """          <!-- SERVICE ROW .06: COMING SOON -->
          <a href="med-spa-website-design.html" class="service-row is-soon" id="website-design" aria-label="Website Design — Coming Soon">
            <div class="service-col-title">
              <div class="service-status-row">
                <span class="service-num">.06 ──</span>
                <span class="service-status-badge is-soon">COMING SOON</span>
              </div>"""

new_row_06 = """          <!-- SERVICE ROW .06: AVAILABLE NOW -->
          <a href="med-spa-website-design.html" class="service-row is-available" id="website-design" aria-label="Website Design — Available Now">
            <div class="service-col-title">
              <div class="service-status-row">
                <span class="service-num">.06 ──</span>
                <span class="service-status-badge is-available">AVAILABLE NOW</span>
              </div>"""

if old_row_06 in s_content:
    s_content = s_content.replace(old_row_06, new_row_06)
    print("Updated services.html row .06 successfully!")
    with open(services_html_path, 'w', encoding='utf-8') as f:
        f.write(s_content)
else:
    print("WARNING: old_row_06 not found in services.html, checking pattern match...")

# 2. Update navigation dropdown in all other html files (except med-spa-website-design files which are already current)
# Root files:
pattern_root_desktop = '<a href="med-spa-website-design.html" role="menuitem" class="nav-dropdown-link is-soon"><span>Website Design</span><span class="nav-soon-badge">COMING SOON</span></a>'
replace_root_desktop = '<a href="med-spa-website-design.html" role="menuitem" class="nav-dropdown-link is-available"><span>Website Design</span></a>'

pattern_root_mobile = '<a href="med-spa-website-design.html" class="mobile-dropdown-link is-soon"><span>Website Design</span><span class="mobile-soon-badge">COMING SOON</span></a>'
replace_root_mobile = '<a href="med-spa-website-design.html" class="mobile-dropdown-link is-available"><span>Website Design</span></a>'

# Subdirectory files (../):
pattern_sub_desktop = '<a href="../med-spa-website-design.html" role="menuitem" class="nav-dropdown-link is-soon"><span>Website Design</span><span class="nav-soon-badge">COMING SOON</span></a>'
replace_sub_desktop = '<a href="../med-spa-website-design.html" role="menuitem" class="nav-dropdown-link is-available"><span>Website Design</span></a>'

pattern_sub_mobile = '<a href="../med-spa-website-design.html" class="mobile-dropdown-link is-soon"><span>Website Design</span><span class="mobile-soon-badge">COMING SOON</span></a>'
replace_sub_mobile = '<a href="../med-spa-website-design.html" class="mobile-dropdown-link is-available"><span>Website Design</span></a>'

updated_count = 0
for f in html_files:
    if "scratch" in f or "review" in f:
        continue
    rel = os.path.relpath(f, base_dir)
    # Don't overwrite med-spa-website-design where it should be is-current
    if rel in ["med-spa-website-design.html", os.path.join("med-spa-website-design", "index.html")]:
        continue

    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    modified = False
    if pattern_root_desktop in c:
        c = c.replace(pattern_root_desktop, replace_root_desktop)
        modified = True
    if pattern_root_mobile in c:
        c = c.replace(pattern_root_mobile, replace_root_mobile)
        modified = True
    if pattern_sub_desktop in c:
        c = c.replace(pattern_sub_desktop, replace_sub_desktop)
        modified = True
    if pattern_sub_mobile in c:
        c = c.replace(pattern_sub_mobile, replace_sub_mobile)
        modified = True

    if modified:
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(c)
        updated_count += 1
        print(f"Updated dropdown in {rel}")

print(f"Total files updated: {updated_count}")
