import os

print("Searching for images in workspace...")
for root, dirs, files in os.walk('.'):
    # skip .git or node_modules
    if any(p in root for p in ['.git', 'node_modules', '.gemini']):
        continue
    for f in files:
        if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
            full = os.path.join(root, f)
            print(f"{full} ({os.path.getsize(full)} bytes)")

