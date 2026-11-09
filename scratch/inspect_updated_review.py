from PIL import Image

def trim_bottom(path, out_path, min_pad=40):
    im = Image.open(path).convert('RGB')
    bg = im.getpixel((0, im.height - 1))
    content_y = im.height
    for y in range(im.height - 1, 0, -1):
        row = [im.getpixel((x, y)) for x in range(0, im.width, 10)]
        if any(abs(p[0] - bg[0]) > 10 or abs(p[1] - bg[1]) > 10 or abs(p[2] - bg[2]) > 10 for p in row):
            content_y = y
            break
    h = min(im.height, content_y + min_pad)
    cropped = im.crop((0, 0, im.width, h))
    cropped.save(out_path, optimize=True)
    print(f"{path} trimmed from {im.size} to {cropped.size} (content bottom: {content_y})")
    return cropped

d_im = trim_bottom('review/desktop_about.png', 'review/desktop_about.png')
t_im = trim_bottom('review/tablet_about.png', 'review/tablet_about.png')
m_im = trim_bottom('review/mobile_about.png', 'review/mobile_about.png')

# Detailed verification crops from desktop
# 1. Header (stacked logo)
d_im.crop((0, 0, d_im.width, 140)).save('scratch/proof_header_stacked.png')

# 2. Team section (all 4 profiles)
# find team section roughly in the middle-bottom
d_im.crop((0, 2000, d_im.width, 2750)).save('scratch/proof_team_profiles.png')

# 3. Footer (horizontal logo)
d_im.crop((0, d_im.height - 600, d_im.width, d_im.height)).save('scratch/proof_footer_horizontal.png')

print("Verification crops generated.")

