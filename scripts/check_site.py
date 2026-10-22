#!/usr/bin/env python3
"""Check the built academic site using only Python's standard library."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import sys
from urllib.parse import unquote, urljoin, urlsplit
import xml.etree.ElementTree as ET


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links = []
        self.ids = set()
        self.classes = Counter()
        self.h1_count = 0
        self.canonical = None
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'):
            self.ids.add(attrs['id'])
        self.classes.update(attrs.get('class', '').split())
        self.h1_count += tag == 'h1'
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonical = attrs.get('href')
        # Metadata references also need to point to valid local assets.
        for attr in ('href', 'src', 'poster'):
            if attrs.get(attr):
                self.links.append(attrs[attr])


def check(site):
    site = site.resolve()
    assert site.is_dir(), f'Missing build directory: {site}'
    pages = {}
    errors = []
    for path in site.rglob('*.html'):
        text = path.read_text()
        pages[path] = Page(text)
        for marker in ('Paper Title Number', 'Teaching experience 1', 'Red Brick University',
                       'academicpages.github.io/files/paper', 'ready-to-fork GitHub Pages template'):
            if marker.lower() in text.lower():
                errors.append(f'{path.relative_to(site)}: demo content {marker!r}')
        if '{{' in text or '{%' in text:
            errors.append(f'{path.relative_to(site)}: unrendered Liquid')
    for path, page in pages.items():
        route = '/' + path.relative_to(site).as_posix()
        for link in page.links:
            parsed = urlsplit(urljoin('https://ooungy.github.io' + route, link))
            if parsed.scheme not in ('http', 'https') or parsed.netloc != 'ooungy.github.io':
                continue
            target = site / unquote(parsed.path).lstrip('/')
            if target.is_dir():
                target /= 'index.html'
            if not target.is_file():
                errors.append(f'{route}: missing local target {link}')
            elif parsed.fragment and target in pages and unquote(parsed.fragment) not in pages[target].ids:
                errors.append(f'{route}: missing anchor {link}')
    for route in ('index.html', 'publications/index.html', 'projects/index.html',
                  'teaching/index.html', 'cv/index.html', '404.html'):
        path = site / route
        assert path in pages, f'Missing required page: {route}'
        assert pages[path].h1_count == 1, f'{route}: expected exactly one h1'
    home = pages[site / 'index.html']
    assert {'about', 'research', 'publications', 'projects', 'teaching', 'contact'} <= home.ids
    assert home.canonical == 'https://ooungy.github.io/', home.canonical
    source = Path(__file__).resolve().parents[1]
    publication_count = len(list((source / '_publications').glob('*.md')))
    project_count = len(list((source / '_portfolio').glob('*.md')))
    assert publication_count > 0 and project_count > 0, 'Expected real content'
    assert pages[site / 'publications/index.html'].classes['publication-entry'] == publication_count
    assert pages[site / 'projects/index.html'].classes['project-entry'] == project_count
    assert (site / 'files/eunji-woo-cv.pdf').read_bytes().startswith(b'%PDF-')
    assert (site / 'assets/css/main.css').stat().st_size > 1000
    sitemap = ET.parse(site / 'sitemap.xml')
    locations = sitemap.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
    assert locations and all(loc.text.startswith('https://ooungy.github.io/') for loc in locations)
    assert not any('paper-title-number' in loc.text or 'teaching-1' in loc.text for loc in locations)
    assert ET.parse(site / 'feed.xml').getroot().tag == '{http://www.w3.org/2005/Atom}feed'
    if errors:
        raise AssertionError('\n'.join(errors))
    print(f'PASS: {len(pages)} HTML pages; all local links, assets and anchors resolve.')
    print(f'PASS: {publication_count} publications, {project_count} projects, six homepage sections, CV PDF, canonical URL, sitemap and feed.')


if __name__ == '__main__':
    check(Path(sys.argv[1] if len(sys.argv) > 1 else '_site'))
