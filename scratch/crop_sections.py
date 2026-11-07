from PIL import Image

im = Image.open(r'C:\Users\riyas\.gemini\antigravity\brain\91a1ccde-d165-4dfe-810e-513091b2e231\.user_uploaded\media_1794049842470_6953d09f.jpg')
w, h = im.size

sections = [
    ('sec1_hero', 0, int(h * 0.28)),
    ('sec2_story', int(h * 0.28), int(h * 0.48)),
    ('sec3_think', int(h * 0.48), int(h * 0.65)),
    ('sec4_feels', int(h * 0.65), int(h * 0.79)),
    ('sec5_team_cta', int(h * 0.79), h),
]

for name, y1, y2 in sections:
    c = im.crop((0, y1, w, y2))
    c.save(f'scratch/about_{name}.png')
    print(f"Saved scratch/about_{name}.png ({w}x{y2-y1})")

