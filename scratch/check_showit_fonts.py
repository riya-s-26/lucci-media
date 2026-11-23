import re

with open(r'c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\luccimedia.html', 'r', encoding='utf-8') as f:
    html = f.read()

# find font styles or font definitions
font_tags = re.findall(r'<style[^>]*>.*?</style>', html, re.DOTALL)
for s in font_tags:
    if 'Nothing You Could Do' in s or 'font-family' in s:
        # find lines with font-family
        for line in s.splitlines():
            if 'font-family' in line and ('Title' in line or 'Heading' in line or 'heading' in line or 'title' in line or 'st-' in line):
                print(line.strip())
