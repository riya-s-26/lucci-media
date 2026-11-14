import glob

for ext in ["*.html", "*.js", "*.css"]:
    for fpath in glob.glob(ext):
        with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
        for idx, line in enumerate(lines, 1):
            arrows = [(c, hex(ord(c))) for c in line if 0x2190 <= ord(c) <= 0x21FF or 0x2700 <= ord(c) <= 0x27BF]
            if arrows:
                print(f"{fpath}:{idx}: {arrows} -> {line.strip()[:80]}")

