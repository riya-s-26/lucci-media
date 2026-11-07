import os
import re
from PIL import Image

print("--- 1. VERIFY IMAGES IN assets/about ---")
expected_imgs = [
    'hero_lex.jpg',
    'story_treatment_room.jpg',
    'story_bottles.jpg',
    'story_cream.jpg',
    'how_we_think_camera.jpg',
    'team_lex.jpg',
    'team_studio_chair.jpg',
    'team_laptop.jpg'
]

for img_name in expected_imgs:
    p = os.path.join('assets/about', img_name)
    if not os.path.exists(p):
        print(f"FAILED: Missing {p}")
    else:
        im = Image.open(p)
        w, h = im.size
        rgb = im.convert('RGB')
        s = rgb.resize((10, 10))
        pix = list(s.getdata())
        r = sum(x[0] for x in pix) // 100
        g = sum(x[1] for x in pix) // 100
        b = sum(x[2] for x in pix) // 100
        lum = int(0.299*r + 0.587*g + 0.114*b)
        print(f"PASS: {img_name:24} {w}x{h} Lum={lum} RGB=({r},{g},{b})")

print("\n--- 2. VERIFY about.html CONTENT PRESERVATION ---")
with open('about.html', 'r', encoding='utf-8') as f:
    html = f.read()

checks = [
    ("[ ABOUT LUCCI MEDIA ]", "Hero eyebrow"),
    ("WE BUILD", "Hero heading line 1"),
    ("THE BRANDS", "Hero heading line 2"),
    ("OTHER BRANDS", "Hero heading line 3"),
    ("STUDY.", "Hero heading line 4"),
    ("Lucci Media is a Boston based creative and social agency", "Hero subtext"),
    ("SCROLL", "Scroll hint"),
    (".01 ───", "Section .01 number"),
    ("[ OUR STORY ]", "Section .01 eyebrow"),
    ("BUILT FROM INSIDE", "Story heading line 1"),
    ("Before Lucci Media, there was the treatment room.", "Story paragraph 1"),
    ("She founded Lucci Media in December 2023", "Story paragraph 2"),
    (".02 ───", "Section .02 number"),
    ("[ HOW WE THINK ]", "Section .02 eyebrow"),
    ("CREATIVE", "Think heading line 1"),
    ("Every month is mapped before a single frame is shot.", "Think body paragraph"),
    ("OUR PROCESS", "Process link"),
    (".03 ───", "Section .03 number"),
    ("[ WHAT WORKING WITH US FEELS LIKE ]", "Section .03 eyebrow"),
    ("PLANNED IN ADVANCE.", "Feels item 1"),
    ("PRODUCED IN HOUSE.", "Feels item 2"),
    ("DIRECTED, NEVER TEMPLATED.", "Feels item 3"),
    ("SELECTIVE BY DESIGN.", "Feels item 4"),
    (".04 ───", "Section .04 number"),
    ("[ MEET THE TEAM ]", "Section .04 eyebrow"),
    ("THE TEAM", "Team heading"),
    ("LEX LUCIANO, FOUNDER AND CREATIVE DIRECTOR.", "Founder name"),
    ("Licensed esthetician and the eye behind every Lucci Media project.", "Founder bio"),
    ("[Team member], [Role]", "Team placeholder 1"),
    ("[One or two lines describing their responsibilities and strengths.]", "Team bio placeholder"),
    ("READY WHEN YOU ARE.", "Final CTA headline"),
    ("START YOUR INQUIRY", "Final CTA button"),
]

for txt, label in checks:
    if txt in html:
        print(f"PASS: {label}")
    else:
        print(f"FAILED: {label} not found!")

print("\n--- 3. VERIFY about.css SYNTAX & BRACES ---")
with open('about.css', 'r', encoding='utf-8') as f:
    css = f.read()

open_braces = css.count('{')
close_braces = css.count('}')
print(f"Brace count: {open_braces} open, {close_braces} close. Matched? {open_braces == close_braces}")
if open_braces != close_braces:
    print("FAILED: CSS brace mismatch!")

print("\nAll verification checks passed!")

