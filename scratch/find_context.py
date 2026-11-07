with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if any(k in l for k in ['lex-portrait-main', 'lex-studio-pose', 'founder-lex', 'lucci-bts', 'behind-the-lens', 'product-content']):
        print(f"Line {i+1}: {l.strip()[:100]}")

