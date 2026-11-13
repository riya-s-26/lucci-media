from PIL import Image

im15 = Image.open('scratch/ticker_700_15_desktop.png')
crop15 = im15.crop((520, 60, 1400, 105))
crop15.save('scratch/detected_700_15.png')
print('Saved detected_700_15.png')

