with open(r'c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\luccimedia.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'Nothing You Could Do' in line:
        print(f"Line {i+1}:")
        print(line[:200])
        for j in range(max(0, i-5), min(len(lines), i+15)):
            if 'data-sid' in lines[j] or 'sie-' in lines[j] or '<p' in lines[j] or '<h' in lines[j] or '<span' in lines[j]:
                print(f"  [{j+1}] {lines[j].strip()[:150]}")
