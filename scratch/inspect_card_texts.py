from PIL import Image

for i in range(1, 5):
    im = Image.open(f'scratch/card_{i}_visible.png')
    # Save the text area at the bottom of the card
    text_crop = im.crop((0, int(im.width * 4 / 3), im.width, im.height))
    text_crop.save(f'scratch/card_{i}_text.png')
    print(f"Card {i} text area size: {text_crop.size}")

