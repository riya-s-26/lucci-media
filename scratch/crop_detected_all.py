from PIL import Image

for w in ['400', '500', '600', '700']:
    im = Image.open(f'scratch/ticker_{w}_14_desktop.png')
    crop = im.crop((520, 60, 1400, 105))
    crop.save(f'scratch/detected_{w}.png')

print('Saved detected crops')

