from PIL import Image

for i in range(1, 5):
    im = Image.open(f'scratch/card_{i}_text.png')
    diff = sum(1 for p in im.getdata() if p != (253, 253, 252))
    print(f"Card {i} text non-bg: {diff}")

