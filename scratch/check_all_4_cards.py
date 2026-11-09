from PIL import Image

im = Image.open('review/desktop_about.png').convert('RGB')
# Team section is roughly y: 2200 to 2900
team_crop = im.crop((0, 2200, im.width, 2900))
team_crop.save('scratch/team_section_crop.png')

w_page = 1240
start_x = (im.width - w_page) // 2
card_w = (w_page - 3 * 28) // 4

for i in range(4):
    cx = start_x + i * (card_w + 28)
    card = team_crop.crop((cx, 80, cx + card_w, team_crop.height - 20))
    card.save(f'scratch/card_{i+1}_visible.png')
    dark = sum(1 for p in card.getdata() if p[0] < 50 and p[1] < 50 and p[2] < 50)
    print(f"Profile card {i+1}: dark pixels = {dark}")

