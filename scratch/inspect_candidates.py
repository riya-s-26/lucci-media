import os
from PIL import Image

candidates = {
    # Campaign Shoots
    'campaign_hero_cand1': 'scratch/dropbox_extracted/IMG_2247.jpg', # on set shoot with softbox & model
    'campaign_hero_cand2': 'scratch/dropbox_extracted/DSC08037.JPG', # creative directors at moodboard
    'campaign_hero_cand3': 'scratch/dropbox_extracted/IMG_4088.JPG', # studio loft setup
    'campaign_details_cand1': 'scratch/dropbox_extracted/DSC08037.JPG', # moodboard planning
    'campaign_details_cand2': 'scratch/dropbox_extracted/IMG_8567.jpg', # camera screen review on set
    'campaign_details_cand3': 'scratch/dropbox_extracted/IMG_2560.JPG', # photographer shooting
    'campaign_proof_cand1': 'scratch/dropbox_extracted/Work/DSC06394.JPG', # skincare products
    'campaign_proof_cand2': 'scratch/dropbox_extracted/Work/IMG_2600.jpg', # 4 beauty campaign models
    'campaign_proof_cand3': 'scratch/dropbox_extracted/Work/IMG_5893.JPG', # ZO skincare bottles

    # Brand Identity
    'brand_hero_cand1': 'scratch/dropbox_extracted/IMG_9969.JPG', # gold foil brand stationery presentation
    'brand_hero_cand2': 'scratch/dropbox_extracted/DSC08107.JPG', # brand strategy book flatlay
    'brand_hero_cand3': 'scratch/dropbox_extracted/IMG_0020.JPG', # brand flatlay
    'brand_details_cand1': 'scratch/dropbox_extracted/DSC08232.JPG', # luxury branded shipping boxes
    'brand_details_cand2': 'scratch/dropbox_extracted/DSC08171.jpg', # brand strategy team review
    'brand_details_cand3': 'scratch/dropbox_extracted/IMG_9960.JPG', # branded boxes flatlay

    # Website Design
    'website_hero_cand1': 'scratch/dropbox_extracted/Tezza-3818.jpg', # laptop on floor with Lucci Media design
    'website_hero_cand2': 'scratch/dropbox_extracted/Templates/LANDSCAPE TEMPLATES - 1.JPG', # website landscape templates
    'website_hero_cand3': 'scratch/dropbox_extracted/Templates/LANDSCAPE TEMPLATES - 5.JPG', # beauty site template layout
    'website_details_cand1': 'scratch/dropbox_extracted/Templates/LANDSCAPE TEMPLATES - 6.JPG', # digital website panels
    'website_details_cand2': 'scratch/dropbox_extracted/Templates/LANDSCAPE TEMPLATES - 7.JPG', # digital website panels
    'website_details_cand3': 'scratch/dropbox_extracted/Work/IMG_2993.JPG', # founder on sofa with laptop
}

os.makedirs('scratch/candidates_preview', exist_ok=True)
for name, path in candidates.items():
    if os.path.exists(path):
        im = Image.open(path)
        im.thumbnail((800, 800))
        out_p = f'scratch/candidates_preview/{name}.jpg'
        im.convert('RGB').save(out_p, quality=85)
        print(f'{name}: {path} ({im.size})')
