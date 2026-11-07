import re

# 1. Check index.html nav
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

expected_nav = ['HOME', 'ABOUT', 'SERVICES', 'THE WORK', 'OUR STUDIO', 'INQUIRE']
desktop_nav_match = re.search(r'<nav class="desktop-nav"[^>]*>(.*?)</nav>', index_html, re.DOTALL)
assert desktop_nav_match, "desktop-nav not found in index.html"
desktop_links = re.findall(r'<a [^>]*>([^<]+)</a>', desktop_nav_match.group(1))
print("Index Desktop Nav links:", desktop_links)
assert desktop_links == expected_nav, f"Expected {expected_nav}, got {desktop_links}"

# 2. Check about.html
with open('about.html', 'r', encoding='utf-8') as f:
    about_html = f.read()

about_nav_match = re.search(r'<nav class="desktop-nav"[^>]*>(.*?)</nav>', about_html, re.DOTALL)
assert about_nav_match, "desktop-nav not found in about.html"
about_links = re.findall(r'<a [^>]*>([^<]+)</a>', about_nav_match.group(1))
print("About Desktop Nav links:", about_links)
assert about_links == expected_nav, f"Expected {expected_nav}, got {about_links}"

# Check Section 1: Hero
assert "[ ABOUT LUCCI MEDIA ]" in about_html
assert "WE BUILD" in about_html
assert "THE BRANDS" in about_html
assert "OTHER BRANDS" in about_html
assert "STUDY." in about_html
assert "Lucci Media is a Boston based creative and social agency for beauty, wellness and lifestyle brands" in about_html
assert "SCROLL" in about_html
assert "hero_lex.jpg" in about_html

# Check Section 2: Our Story
assert ".01" in about_html
assert "[ OUR STORY ]" in about_html
assert "BUILT FROM INSIDE" in about_html
assert "THE TREATMENT" in about_html
assert "ROOM." in about_html
assert "Before Lucci Media, there was the treatment room." in about_html
assert "She founded Lucci Media in December 2023 to close that gap." in about_html
assert "story_treatment_room.jpg" in about_html
assert "story_bottles.jpg" in about_html
assert "story_cream.jpg" in about_html

# Check Section 3: How We Think
assert ".02" in about_html
assert "[ HOW WE THINK ]" in about_html
assert "CREATIVE" in about_html
assert "DIRECTION" in about_html
assert "WITH A BUSINESS" in about_html
assert "PLAN BEHIND IT." in about_html
assert "Every month is mapped before a single frame is shot." in about_html
assert "OUR PROCESS" in about_html
assert "how_we_think_camera.jpg" in about_html

# Check Section 4: What Working With Us Feels Like
assert ".03" in about_html
assert "[ WHAT WORKING WITH US FEELS LIKE ]" in about_html
assert "WHAT" in about_html
assert "WORKING" in about_html
assert "WITH US" in about_html
assert "FEELS LIKE." in about_html
assert "PLANNED IN ADVANCE." in about_html
assert "PRODUCED IN HOUSE." in about_html
assert "DIRECTED, NEVER TEMPLATED." in about_html
assert "SELECTIVE BY DESIGN." in about_html
assert "Your month is strategized, approved and scheduled before it starts." in about_html
assert "One team handles direction, filming, editing and publishing" in about_html
assert "We don't recycle formats across clients." in about_html
assert "We cap the number of partners we take on" in about_html

# Check Section 5: Meet the Team
assert ".04" in about_html
assert "[ MEET THE TEAM ]" in about_html
assert "THE TEAM" in about_html
assert "BEHIND THE FEED." in about_html
assert "LEX LUCIANO, FOUNDER AND CREATIVE DIRECTOR." in about_html
assert "Licensed esthetician and the eye behind every Lucci Media project." in about_html
assert "[Team member], [Role]" in about_html
assert "[One or two lines describing their responsibilities and strengths.]" in about_html
assert "team_lex.jpg" in about_html
assert "team_studio_chair.jpg" in about_html
assert "team_laptop.jpg" in about_html

# Check Section 6: Final CTA
assert "READY WHEN YOU ARE." in about_html
assert "START YOUR INQUIRY" in about_html

# 3. Check coming-soon.html
with open('coming-soon.html', 'r', encoding='utf-8') as f:
    cs_html = f.read()

assert "COMING SOON" in cs_html
assert "BACK TO HOME" in cs_html
assert "desktop-nav" in cs_html

# 4. Check CSS files
for css_file in ['styles.css', 'about.css', 'coming-soon.css']:
    with open(css_file, 'r', encoding='utf-8') as f:
        c = f.read()
    open_b = c.count('{')
    close_b = c.count('}')
    assert open_b == close_b, f"Mismatched braces in {css_file}: {open_b} open vs {close_b} close"
    print(f"{css_file} braces balanced ({open_b}).")

print("ALL VERIFICATION CHECKS PASSED PERFECTLY!")

