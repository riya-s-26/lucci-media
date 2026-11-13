from PIL import Image

im400 = Image.open('scratch/ticker_400_14_desktop.png')
im500 = Image.open('scratch/ticker_500_14_desktop.png')
im700 = Image.open('scratch/ticker_700_14_desktop.png')

# The ticker in ticker_*_desktop.png starts around x=740, y=70 to 130
crop400 = im400.crop((740, 70, 1400, 130))
crop500 = im500.crop((740, 70, 1400, 130))
crop700 = im700.crop((740, 70, 1400, 130))

crop400.save('scratch/crop400.png')
crop500.save('scratch/crop500.png')
crop700.save('scratch/crop700.png')
print('Cropped successfully')

