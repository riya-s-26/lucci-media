from PIL import Image

im = Image.open('scratch/ticker_400_14_desktop.png')
print('Image size:', im.size)

# Find coordinates of dark pixels
coords = []
for y in range(im.height):
    for x in range(im.width):
        r, g, b = im.getpixel((x, y))[:3]
        if r < 150 and g < 150 and b < 150: # dark text
            coords.append((x, y))

if coords:
    min_x = min(c[0] for c in coords)
    max_x = max(c[0] for c in coords)
    min_y = min(c[1] for c in coords)
    max_y = max(c[1] for c in coords)
    print(f'Bounding box of text: x: [{min_x}, {max_x}], y: [{min_y}, {max_y}]')
    
    # Let's filter for text in the ticker area (x > 500)
    ticker_coords = [c for c in coords if c[0] > 500]
    if ticker_coords:
        t_min_x = min(c[0] for c in ticker_coords)
        t_max_x = max(c[0] for c in ticker_coords)
        t_min_y = min(c[1] for c in ticker_coords)
        t_max_y = max(c[1] for c in ticker_coords)
        print(f'Ticker text: x: [{t_min_x}, {t_max_x}], y: [{t_min_y}, {t_max_y}]')
        crop_t = im.crop((t_min_x - 10, t_min_y - 10, t_max_x + 10, t_max_y + 10))
        crop_t.save('scratch/exact_detected_ticker.png')
else:
    print('No text detected')

