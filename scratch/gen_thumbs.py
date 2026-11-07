import os
from PIL import Image

imgs = {
    'about_portrait': 'assets/about/about_portrait.jpg',
    'lex_portrait_main': 'assets/lucci/lex-portrait-main.jpg',
    'lex_studio_pose': 'assets/lucci/lex-studio-pose.jpg',
    'lex_camera_onset': 'assets/lucci/lex-camera-onset.jpg',
    'founder_lex': 'assets/founder-lex.webp',
    'hero_lex_portrait': 'assets/hero-lex-portrait.jpg',
    'lucci_bts_shoot': 'assets/lucci/lucci-bts-shoot.jpg',
    'lucci_bts_studio': 'assets/lucci/lucci-bts-studio.jpg',
    'lucci_bts_table': 'assets/lucci/lucci-bts-table.jpg',
    'bot_04': 'assets/archive/bot_04.jpg',
    'bot_05': 'assets/archive/bot_05.jpg',
    'bot_09': 'assets/archive/bot_09.jpg',
    'service_01': 'assets/services/service_01.jpg',
    'service_02': 'assets/services/service_02.jpg',
    'service_03': 'assets/services/service_03.jpg',
}

for name, path in imgs.items():
    if os.path.exists(path):
        im = Image.open(path)
        im.thumbnail((300, 300))
        im.save(f'scratch/thumb_{name}.jpg')
        print(f'Saved thumb_{name}.jpg')

