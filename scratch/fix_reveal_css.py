with open('about.css', 'r', encoding='utf-8') as f:
    css = f.read()

# add reveal safeguard to about.css
if '.about-page-main [data-reveal]' not in css:
    css += "\n.about-page-main [data-reveal] { opacity: 1 !important; transform: none !important; }\n"
    with open('about.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Added data-reveal visibility rule to about.css")

