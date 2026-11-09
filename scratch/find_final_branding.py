import os

for root, dirs, files in os.walk('.'):
    for f in files:
        if 'final-10' in f.lower() or 'final-02' in f.lower() or 'final' in f.lower():
            print(os.path.join(root, f))

