# Let's inspect where lex-studio-pose.jpg is used in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'lex-studio-pose' in l:
        print(f"Index line {i+1}: {l.strip()}")

