import os
import glob
import re

base_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media"
html_files = glob.glob(os.path.join(base_dir, "**", "*.html"), recursive=True)

# 1. Update services.html row .07
services_html_path = os.path.join(base_dir, "services.html")
with open(services_html_path, 'r', encoding='utf-8') as f:
    s_content = f.read()

old_row_07 = """          <!-- SERVICE ROW .07: COMING SOON -->
          <a href="google-business-profile-management.html" class="service-row is-soon" id="google-business-profile" aria-label="Google Business Profile — Coming Soon">
            <div class="service-col-title">
              <div class="service-status-row">
                <span class="service-num">.07 ──</span>
                <span class="service-status-badge is-soon">COMING SOON</span>
              </div>"""

new_row_07 = """          <!-- SERVICE ROW .07: AVAILABLE NOW -->
          <a href="google-business-profile-management.html" class="service-row is-available" id="google-business-profile" aria-label="Google Business Profile — Available Now">
            <div class="service-col-title">
              <div class="service-status-row">
                <span class="service-num">.07 ──</span>
                <span class="service-status-badge is-available">AVAILABLE NOW</span>
              </div>"""

if old_row_07 in s_content:
    s_content = s_content.replace(old_row_07, new_row_07)
    print("Updated services.html row .07 successfully!")
    with open(services_html_path, 'w', encoding='utf-8') as f:
        f.write(s_content)
else:
    print("WARNING: old_row_07 not found in services.html")

# 2. Update navigation dropdown in all other html files (except google-business-profile-management where it is current)
pattern_root_desktop = '<a href="google-business-profile-management.html" role="menuitem" class="nav-dropdown-link is-soon"><span>Google Business Profile</span><span class="nav-soon-badge">COMING SOON</span></a>'
replace_root_desktop = '<a href="google-business-profile-management.html" role="menuitem" class="nav-dropdown-link is-available"><span>Google Business Profile</span></a>'

pattern_root_mobile = '<a href="google-business-profile-management.html" class="mobile-dropdown-link is-soon"><span>Google Business Profile</span><span class="mobile-soon-badge">COMING SOON</span></a>'
replace_root_mobile = '<a href="google-business-profile-management.html" class="mobile-dropdown-link is-available"><span>Google Business Profile</span></a>'

pattern_sub_desktop = '<a href="../google-business-profile-management.html" role="menuitem" class="nav-dropdown-link is-soon"><span>Google Business Profile</span><span class="nav-soon-badge">COMING SOON</span></a>'
replace_sub_desktop = '<a href="../google-business-profile-management.html" role="menuitem" class="nav-dropdown-link is-available"><span>Google Business Profile</span></a>'

pattern_sub_mobile = '<a href="../google-business-profile-management.html" class="mobile-dropdown-link is-soon"><span>Google Business Profile</span><span class="mobile-soon-badge">COMING SOON</span></a>'
replace_sub_mobile = '<a href="../google-business-profile-management.html" class="mobile-dropdown-link is-available"><span>Google Business Profile</span></a>'

updated_count = 0
for f in html_files:
    if "scratch" in f or "review" in f:
        continue
    rel = os.path.relpath(f, base_dir)
    if rel in ["google-business-profile-management.html", os.path.join("google-business-profile-management", "index.html")]:
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

    # Also handle possible multi-line formatting e.g. in beauty-content-creation
    multi_desk = re.findall(r'<a href="[^"]*google-business-profile-management\.html"[^>]*class="nav-dropdown-link is-soon"[^>]*>[\s\S]*?COMING\s*SOON</span></a>', c)
    for m in multi_desk:
        is_sub = "../" in m
        rep = f'<a href="{"../" if is_sub else ""}google-business-profile-management.html" role="menuitem" class="nav-dropdown-link is-available"><span>Google Business Profile</span></a>'
        c = c.replace(m, rep)
        modified = True

    multi_mob = re.findall(r'<a href="[^"]*google-business-profile-management\.html"[^>]*class="mobile-dropdown-link is-soon"[^>]*>[\s\S]*?COMING\s*SOON</span></a>', c)
    for m in multi_mob:
        is_sub = "../" in m
        rep = f'<a href="{"../" if is_sub else ""}google-business-profile-management.html" class="mobile-dropdown-link is-available"><span>Google Business Profile</span></a>'
        c = c.replace(m, rep)
        modified = True

    if modified:
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(c)
        updated_count += 1
        print(f"Updated dropdown in {rel}")

print(f"Total files updated: {updated_count}")
