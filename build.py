#!/usr/bin/env python3
"""Build HTML output files by expanding <!-- include: path --> markers in templates."""
import re, os

BASE = os.path.dirname(os.path.abspath(__file__))
SRC  = os.path.join(BASE, 'src')

def expand(content, base_dir):
    def replacer(m):
        path = os.path.join(base_dir, m.group(1).strip())
        with open(path) as f:
            return f.read()
    return re.sub(r'<!-- include: (.+?) -->', replacer, content)

targets = [
    ('src/templates/index.html',       'index.html'),
    ('src/templates/print-front.html', 'print-front.html'),
    ('src/templates/print-back.html',  'print-back.html'),
]

for src_rel, out_rel in targets:
    with open(os.path.join(BASE, src_rel)) as f:
        content = f.read()
    content = expand(content, SRC)
    out_path = os.path.join(BASE, out_rel)
    with open(out_path, 'w') as f:
        f.write(content)
    print(f'  built {out_rel}')
