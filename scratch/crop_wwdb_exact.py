from PIL import Image

im = Image.open('scratch/temp_index_full.png')
crop = im.crop((0, 1200, 1440, 1700))
crop.save('scratch/actual_wwdb_headline.png')
print('Saved actual_wwdb_headline.png')

