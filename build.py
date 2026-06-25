#!/usr/bin/env python3
"""Build HTML and PDF output files from src/ templates.

Usage:
  python3 build.py        # HTML + PDF
  python3 build.py --html # HTML only
"""
import re, os, sys, subprocess, threading, time, functools
import http.server, socketserver

BASE   = os.path.dirname(os.path.abspath(__file__))
SRC    = os.path.join(BASE, 'src')
PORT   = 8791
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

HTML_TARGETS = [
    ('src/templates/index.html',       'build/index.html'),
    ('src/templates/print-front.html', 'build/print-front.html'),
    ('src/templates/print-back.html',  'build/print-back.html'),
]

PDF_TARGETS = [
    ('build/print-front.html', 'dist/front.pdf'),
    ('build/print-back.html',  'dist/back.pdf'),
]

def expand(content, base_dir):
    def replacer(m):
        path = os.path.join(base_dir, m.group(1).strip())
        with open(path) as f:
            return f.read()
    return re.sub(r'<!-- include: (.+?) -->', replacer, content)

def build_html():
    os.makedirs(os.path.join(BASE, 'build'), exist_ok=True)
    for src_rel, out_rel in HTML_TARGETS:
        with open(os.path.join(BASE, src_rel)) as f:
            content = f.read()
        content = expand(content, SRC)
        with open(os.path.join(BASE, out_rel), 'w') as f:
            f.write(content)
        print(f'  html  {out_rel}')

def build_pdf():
    os.makedirs(os.path.join(BASE, 'dist'), exist_ok=True)

    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=BASE)
    handler.log_message = lambda *a: None
    with socketserver.TCPServer(('', PORT), handler) as httpd:
        t = threading.Thread(target=httpd.serve_forever)
        t.daemon = True
        t.start()
        time.sleep(0.5)

        for src_html, out_pdf in PDF_TARGETS:
            out_path = os.path.join(BASE, out_pdf)
            subprocess.run([
                CHROME,
                '--headless=new',
                f'--print-to-pdf={out_path}',
                '--no-pdf-header-footer',
                '--print-to-pdf-no-header',
                f'http://localhost:{PORT}/{src_html}',
            ], capture_output=True)
            print(f'  pdf   {out_pdf}')

        httpd.shutdown()

if __name__ == '__main__':
    html_only = '--html' in sys.argv
    build_html()
    if not html_only:
        build_pdf()
