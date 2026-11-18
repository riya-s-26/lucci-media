import re

files = ['index.html', 'about.html', 'services.html', 'coming-soon.html', 'inquire.html']

for f_name in files:
    with open(f'c:/xampp/htdocs/luci/{f_name}', 'r', encoding='utf-8') as f:
        content = f.read()

    inquire_links = re.findall(r'href=["\']([^"\']*inquire[^"\']*)["\']', content, re.IGNORECASE)
    coming_soon_inquire = re.findall(r'href=["\']([^"\']*coming-soon\.html\?page=Inquire[^"\']*)["\']', content, re.IGNORECASE)
    print(f"=== {f_name} ===")
    print(f"Inquire links count: {len(inquire_links)} -> {inquire_links}")
    print(f"Coming soon inquire links: {len(coming_soon_inquire)}")
