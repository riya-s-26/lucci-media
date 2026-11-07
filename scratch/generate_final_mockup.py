import os
from PIL import Image, ImageDraw, ImageFont

# 1. Load original mockup
ref_path = r'C:\Users\riyas\.gemini\antigravity\brain\91a1ccde-d165-4dfe-810e-513091b2e231\.user_uploaded\media_1794049842470_6953d09f.jpg'
orig_mockup = Image.open(ref_path).convert('RGB')
w_1x, h_1x = orig_mockup.size # 682 x 1024

# Scale 2x with high quality Lanczos for crisp rendering
w_2x, h_2x = w_1x * 2, h_1x * 2 # 1364 x 2048
mockup_2x = orig_mockup.resize((w_2x, h_2x), Image.Resampling.LANCZOS)

# -------------------------------------------------------------------------
# CHANGE 1: REPLACE HERO IMAGE
# Hero bounding box at 2x: x1 = 560, y1 = 90, w = 804, h = 470
# -------------------------------------------------------------------------
hero_src = Image.open('assets/lucci/lucci-bts-shoot.jpg').convert('RGB')
hw, hh = hero_src.size
target_ratio = 804 / 470
target_h_crop = int(hw / target_ratio)
start_y = (hh - target_h_crop) // 2
hero_cropped = hero_src.crop((0, start_y, hw, start_y + target_h_crop)).resize((804, 470), Image.Resampling.LANCZOS)

# Paste hero image exactly at (560, 90)
mockup_2x.paste(hero_cropped, (560, 90))

# -------------------------------------------------------------------------
# CHANGE 2: REPLACE SECTION 03 CONTENT
# Section 03 rows at 2x:
# x: 600 to 1290 (width = 690)
# y: 1334 to 1564 (height = 230)
# -------------------------------------------------------------------------

# Clean the rows background with the exact off-white color (252, 252, 251)
bg_color = (252, 252, 251)
draw = ImageDraw.Draw(mockup_2x)

# Erase old rows area
x_start_rows = 595
x_end_rows = 1295
y_start_rows = 1332
y_end_rows = 1568
draw.rectangle([x_start_rows, y_start_rows, x_end_rows, y_end_rows], fill=bg_color)

# Fonts
font_num = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 13)
font_head = ImageFont.truetype('scratch/fonts/shapiro.ttf', 12)
font_desc = ImageFont.truetype(r'C:\Windows\Fonts\segoeui.ttf', 13)

def wrap_text(text, font, max_w, d):
    words = text.split()
    lines = []
    cur = []
    for w in words:
        test = ' '.join(cur + [w])
        bbox = d.textbbox((0, 0), test, font=font)
        if (bbox[2] - bbox[0]) <= max_w:
            cur.append(w)
        else:
            if cur:
                lines.append(' '.join(cur))
                cur = [w]
            else:
                lines.append(w)
                cur = []
    if cur:
        lines.append(' '.join(cur))
    return lines

rows_content = [
    ("01 ───", "PLANNED IN ADVANCE.", "Your month is strategized, approved and scheduled before it starts."),
    ("02 ───", "PRODUCED IN HOUSE.", "One team handles direction, filming, editing and publishing, so nothing gets lost between vendors."),
    ("03 ───", "DIRECTED, NEVER TEMPLATED.", "We don't recycle formats across clients. Your content is built for your brand and nobody else's."),
    ("04 ───", "SELECTIVE BY DESIGN.", "We cap the number of partners we take on so every account gets senior creative attention.")
]

x_col_num = 612
x_col_head = 740
x_col_desc = 975
desc_max_w = 310

divider_color = (212, 210, 207)
num_color = (138, 132, 127)
head_color = (30, 27, 24)
desc_color = (85, 80, 75)

total_rows_h = y_end_rows - y_start_rows
row_h = total_rows_h / 4 # ~59px

# Top divider line
draw.line([(x_col_num, y_start_rows), (x_col_desc + desc_max_w, y_start_rows)], fill=divider_color, width=1)

for i, (num_txt, head_txt, desc_txt) in enumerate(rows_content):
    row_top = y_start_rows + i * row_h
    row_bottom = y_start_rows + (i + 1) * row_h
    text_y = int(row_top + 14)
    
    # Draw number
    draw.text((x_col_num, text_y), num_txt, font=font_num, fill=num_color)
    
    # Draw heading
    draw.text((x_col_head, text_y + 1), head_txt, font=font_head, fill=head_color)
    
    # Draw description lines
    lines = wrap_text(desc_txt, font_desc, desc_max_w, draw)
    for l_idx, line in enumerate(lines):
        draw.text((x_col_desc, text_y + l_idx * 19), line, font=font_desc, fill=desc_color)
    
    # Divider line under row
    draw.line([(x_col_num, int(row_bottom)), (x_col_desc + desc_max_w, int(row_bottom))], fill=divider_color, width=1)

# Save 2x high-res corrected mockup
mockup_2x_path = r'C:\Users\riyas\.gemini\antigravity\brain\91a1ccde-d165-4dfe-810e-513091b2e231\lucci_media_about_mockup_corrected_2x.png'
mockup_2x.save(mockup_2x_path, quality=95)
print("Saved 2x corrected mockup:", mockup_2x_path)

# Also generate native 1x corrected mockup (682 x 1024)
mockup_1x = mockup_2x.resize((w_1x, h_1x), Image.Resampling.LANCZOS)
mockup_1x_path = r'C:\Users\riyas\.gemini\antigravity\brain\91a1ccde-d165-4dfe-810e-513091b2e231\lucci_media_about_mockup_corrected.png'
mockup_1x.save(mockup_1x_path, quality=95)
print("Saved 1x corrected mockup:", mockup_1x_path)

# Also save a copy in the workspace assets/about/ for immediate site serving
mockup_1x.save('assets/about/mockup_corrected.png')
print("Saved assets/about/mockup_corrected.png")

