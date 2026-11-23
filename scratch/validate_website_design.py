import os
import re
from html.parser import HTMLParser

class TagValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.void_elements = {
            'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input',
            'link', 'meta', 'param', 'source', 'track', 'wbr'
        }
        self.errors = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() not in self.void_elements:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag in self.void_elements:
            return
        if not self.stack:
            self.errors.append(f"Unexpected closing tag </{tag}> with empty stack")
            return
        last = self.stack.pop()
        if last != tag:
            self.errors.append(f"Mismatched tag: expected </{last}>, found </{tag}>")

def validate_file(filepath):
    print(f"\n--- Validating {filepath} ---")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Tag validation
    parser = TagValidator()
    parser.feed(content)
    if parser.stack:
        print(f"Unclosed tags remaining on stack: {parser.stack}")
    else:
        print("All HTML tags opened and closed properly! (0 unclosed tags)")

    if parser.errors:
        print("Parser errors found:", parser.errors)
    else:
        print("0 parser errors!")

    # Check referenced local files
    srcs = re.findall(r'src=["\']([^"\']+)["\']', content)
    hrefs = re.findall(r'href=["\']([^"\']+)["\']', content)
    
    file_dir = os.path.dirname(filepath)
    missing = []
    
    for ref in srcs + hrefs:
        # Ignore external or hash or query
        if ref.startswith(('http://', 'https://', '#', 'mailto:', 'tel:')):
            continue
        # Strip query params or hash
        clean_ref = ref.split('?')[0].split('#')[0]
        if not clean_ref:
            continue
        ref_path = os.path.normpath(os.path.join(file_dir, clean_ref))
        if not os.path.exists(ref_path):
            missing.append(ref)

    if missing:
        print("Missing referenced files:", set(missing))
    else:
        print("All local src and href assets exist!")

validate_file(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\med-spa-website-design.html")
validate_file(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\med-spa-website-design\index.html")
