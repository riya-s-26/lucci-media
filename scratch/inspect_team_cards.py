from PIL import Image

im = Image.open('scratch/proof_final_team.png')
print("Team section proof size:", im.size)
# inspect the four cards: each card has width ~280-300px
# Let's save each of the 4 cards individually
# The cards are distributed horizontally across page-wrap (x=100 to 1340)
w_page = 1240
start_x = (im.width - w_page) // 2
card_w = (w_page - 3 * 28) // 4
print("Card width approx:", card_w)

for i in range(4):
    cx = start_x + i * (card_w + 28)
    card_crop = im.crop((cx, 80, cx + card_w, im.height - 20))
    card_crop.save(f'scratch/proof_card_{i+1}.png')
    print(f"Saved scratch/proof_card_{i+1}.png with size {card_crop.size}")

