import os

for f in ['team_studio_chair.jpg', 'team_laptop.jpg', 'team_lex.jpg']:
    p = os.path.join('assets/about', f)
    size = os.path.getsize(p)
    print(f, size)
    # search for exact matching file size elsewhere
    for root, dirs, files in os.walk('.'):
        if 'assets/about' in root: continue
        for other in files:
            op = os.path.join(root, other)
            try:
                if os.path.getsize(op) == size:
                    print(f"  Matches size of: {op}")
            except:
                pass

