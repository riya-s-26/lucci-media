from PIL import Image, ImageDraw, ImageFont

# Load the cropped actual WWDB headline
im_wwdb = Image.open('scratch/actual_wwdb_headline.png').crop((80, 200, 500, 260))

# Load the ticker variations
im_400 = Image.open('scratch/ticker_400_14_desktop.png').crop((750, 60, 1400, 130))
im_500 = Image.open('scratch/ticker_500_14_desktop.png').crop((750, 60, 1400, 130))
im_600 = Image.open('scratch/ticker_600_14_desktop.png').crop((750, 60, 1400, 130))
im_700 = Image.open('scratch/ticker_700_14_desktop.png').crop((750, 60, 1400, 130))

# Create a combined image
canvas = Image.new('RGB', (700, 420), '#FFFFFF')
draw = ImageDraw.Draw(canvas)

draw.text((10, 10), "Actual 'WHAT WE DO BEST':", fill='#000000')
canvas.paste(im_wwdb, (10, 30))

draw.text((10, 100), "Ticker weight 400:", fill='#000000')
canvas.paste(im_400, (10, 120))

draw.text((10, 180), "Ticker weight 500:", fill='#000000')
canvas.paste(im_500, (10, 200))

draw.text((10, 260), "Ticker weight 700:", fill='#000000')
canvas.paste(im_700, (10, 280))

canvas.save('scratch/compare_all_weights.png')
print('Saved scratch/compare_all_weights.png')

