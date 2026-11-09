from PIL import Image

d_im = Image.open('review/desktop_about.png')
# inspect bottom 300 rows
bot_crop = d_im.crop((0, d_im.height - 300, d_im.width, d_im.height))
bot_crop.save('scratch/review_bottom_check.png')

# Let's check mobile bottom as well
m_im = Image.open('review/mobile_about.png')
m_bot_crop = m_im.crop((0, m_im.height - 300, m_im.width, m_im.height))
m_bot_crop.save('scratch/review_m_bottom_check.png')

print("Saved bottom checks")

