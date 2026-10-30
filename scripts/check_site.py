#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Check generated documentation links, assets, and browser-title punctuation."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links, self.ids, self.title = [], set(), ''
        self.in_title = False
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            self.in_title = True
        for key, value in attrs:
            if key in ('href', 'src') and value:
                self.links.append(value)
            if key == 'id':
                self.ids.add(value)

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False

    def handle_data(self, text):
        if self.in_title:
            self.title += text


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else '_build/html').resolve()
    pages = {p.resolve(): Page(p.read_text(encoding='utf-8'))
             for p in root.rglob('*.html')
             if not any(part.startswith('_') for part in p.relative_to(root).parts[:-1])}
    if not pages:
        raise SystemExit(f'No HTML pages found in {root}; build documentation first.')
    errors = []
    for path, page in pages.items():
        if not page.title.strip() or any(s in page.title for s in ('\u2014', '\u2013', '--')):
            errors.append(f'{path.name}: invalid browser title {page.title!r}')
        for link in page.links:
            url = urlsplit(link)
            if url.scheme or url.netloc:
                continue
            target = ((root / unquote(url.path.lstrip('/'))) if url.path.startswith('/')
                      else (path.parent / unquote(url.path))) if url.path else path
            target = target.resolve()
            if target.is_dir():
                target = target / 'index.html'
            if not target.exists():
                errors.append(f'{path.name}: missing local target {link}')
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                errors.append(f'{path.name}: missing anchor {link}')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'Checked {len(pages)} pages: titles, local links, anchors, and assets passed.')


if __name__ == '__main__':
    main()
