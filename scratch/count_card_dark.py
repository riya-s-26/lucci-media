from PIL import Image

im = Image.open('scratch/final_proof_team_section.png').convert('RGB')
w_page = 1240
start_x = (im.width - w_page) // 2
card_w = (w_page - 3 * 28) // 4

for i in range(4):
    cx = start_x + i * (card_w + 28)
    card = im.crop((cx, 0, cx + card_w, im.height))
    dark = sum(1 for p in card.getdata() if p[0] < 50 and p[1] < 50 and p[2] < 50)
    print(f"Profile card {i+1}: dark pixels = {dark}")

