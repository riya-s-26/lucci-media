import os, re

other_pages = [
    'services.html', 'index.html', 'about.html', 'inquire.html',
    'social-media-management-boston.html', 'beauty-content-creation-boston.html',
    'brand-photography-boston.html', 'google-business-profile-boston.html'
]

used_imgs = set()
for p in other_pages:
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', f.read())
            for img in imgs:
                used_imgs.add(os.path.basename(img).lower())

print('Images used in other pages:')
for img in sorted(used_imgs):
    print(' ', img)
