import os

# Search for mentions of brand kit keywords across the project
keywords = ['montserrat tight', 'brand kit', 'brand guide', 'slate', 'ash', 'espresso', 'stone', 'desaturated', 'tactile', 'soph', 'nicole', 'deandra']

for root, dirs, files in os.walk('.'):
    if '.git' in root:
        continue
    for f in files:
        if f.endswith(('.html', '.css', '.js', '.json', '.txt', '.php', '.md')):
            p = os.path.join(root, f)
            try:
                with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                    text = fp.read().lower()
                for kw in keywords:
                    if kw in text:
                        print(f"Keyword '{kw}' found in {p}")
            except:
                pass

