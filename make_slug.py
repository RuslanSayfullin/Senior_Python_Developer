import re

def slugify(s):
    s = s.lower().strip()
    print(s)
    s = re.sub(r'[^\w\s-]', '', s)
    print(s)
    s = re.sub(r'[\s_-]+', '-', s)
    print(s)
    s = re.sub(r'^-+', '', s)
    print(s)

slugify('Hello, World!')
