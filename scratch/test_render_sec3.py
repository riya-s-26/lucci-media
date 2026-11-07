import os
from PIL import Image, ImageDraw, ImageFont

# Let's write a text wrapper helper
def wrap_text(text, font, max_width, draw):
    words = text.split()
    lines = []
    current_line = []
    for word in words:
        test_line = ' '.join(current_line + [word])
        bbox = draw.textbbox((0, 0), test_line, font=font)
        w = bbox[2] - bbox[0]
        if w <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(' '.join(current_line))
                current_line = [word]
            else:
                lines.append(word)
                current_line = []
    if current_line:
        lines.append(' '.join(current_line))
    return lines

# Let's test render the 4 rows on a blank canvas matching sec3_orig_2x size (770 x 285)
canvas = Image.new('RGB', (770, 285), (252, 252, 251))
draw = ImageDraw.Draw(canvas)

# Fonts
font_num = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 14)
font_head = ImageFont.truetype('scratch/fonts/shapiro.ttf', 13)
font_desc = ImageFont.truetype(r'C:\Windows\Fonts\segoeui.ttf', 14)

rows_data = [
    ("01  ───", "PLANNED IN ADVANCE.", "Your month is strategized, approved and scheduled before it starts."),
    ("02  ───", "PRODUCED IN HOUSE.", "One team handles direction, filming, editing and publishing, so nothing gets lost between vendors."),
    ("03  ───", "DIRECTED, NEVER TEMPLATED.", "We don't recycle formats across clients. Your content is built for your brand and nobody else's."),
    ("04  ───", "SELECTIVE BY DESIGN.", "We cap the number of partners we take on so every account gets senior creative attention.")
]

x_start = 75
x_head = 200
x_desc = 400
desc_max_w = 340

divider_color = (215, 213, 210)
num_color = (138, 132, 127)
head_color = (30, 27, 24)
desc_color = (85, 80, 75)

# 4 rows across height 285 -> row_height ~ 68px
row_h = 68
y_top = 10

# Top divider
draw.line([(x_start, y_top), (x_desc + desc_max_w, y_top)], fill=divider_color, width=1)

for i, (num, head, desc) in enumerate(rows_data):
    current_y = y_top + i * row_h
    text_y = current_y + 14
    
    # Draw number
    draw.text((x_start, text_y), num, font=font_num, fill=num_color)
    
    # Draw heading
    # Heading can be multi-word or wrapped if needed
    draw.text((x_head, text_y + 1), head, font=font_head, fill=head_color)
    
    # Draw description wrapped
    lines = wrap_text(desc, font_desc, desc_max_w, draw)
    for j, line in enumerate(lines):
        draw.text((x_desc, text_y + j * 20), line, font=font_desc, fill=desc_color)
    
    # Bottom divider
    div_y = current_y + row_h
    draw.line([(x_start, div_y), (x_desc + desc_max_w, div_y)], fill=divider_color, width=1)

canvas.save('scratch/test_sec3_rendered.png')
print("Saved scratch/test_sec3_rendered.png")

