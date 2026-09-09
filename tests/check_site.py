"""Check static-site destinations, assets and accessible HTML without dependencies.

Run from any directory: python tests/check_site.py
Browser checks for responsive layout and keyboard behaviour complement these tests.
"""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import unittest

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.elements = []

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))


PAGE = Page()
PAGE.feed((ROOT / 'index.html').read_text(encoding='utf-8'))


class SiteChecks(unittest.TestCase):
    def test_unique_ids(self):
        ids = Counter(attrs['id'] for _, attrs in PAGE.elements if 'id' in attrs)
        self.assertFalse([key for key, count in ids.items() if count > 1])

    def test_local_links_and_assets_exist(self):
        ids = {attrs['id'] for _, attrs in PAGE.elements if 'id' in attrs}
        for tag, attrs in PAGE.elements:
            for key in ('href', 'src'):
                if key not in attrs:
                    continue
                value = attrs[key]
                with self.subTest(tag=tag, url=value):
                    self.assertNotIn(value, ('', '#'))
                    self.assertNotIn('your-demo-link', value)
                    url = urlsplit(value)
                    if url.scheme or url.netloc:
                        continue
                    if url.path:
                        target = ROOT / unquote(url.path)
                        self.assertTrue(target.is_file(), f'Missing {target}')
                    if url.fragment and not url.path:
                        self.assertIn(url.fragment, ids)
            if 'srcset' in attrs:
                for candidate in attrs['srcset'].split(','):
                    self.assertTrue((ROOT / candidate.strip().split()[0]).is_file())

    def test_landmarks_and_navigation_relationships(self):
        self.assertEqual(sum(tag == 'main' for tag, _ in PAGE.elements), 1)
        self.assertEqual(sum(tag == 'h1' for tag, _ in PAGE.elements), 1)
        ids = {attrs['id'] for _, attrs in PAGE.elements if 'id' in attrs}
        for tag, attrs in PAGE.elements:
            for reference in ('aria-controls', 'aria-labelledby'):
                for value in attrs.get(reference, '').split():
                    self.assertIn(value, ids)
            if tag == 'nav':
                self.assertIn('aria-label', attrs)

    def test_image_accessibility_and_dimensions(self):
        for tag, attrs in PAGE.elements:
            if tag == 'img':
                with self.subTest(image=attrs.get('src')):
                    self.assertIn('alt', attrs)
                    self.assertGreater(int(attrs['width']), 0)
                    self.assertGreater(int(attrs['height']), 0)

    def test_assets_have_reasonable_transfer_budgets(self):
        budgets = {'favicon.png': 10000, 'portrait-320.webp': 25000,
                   'portrait-640.webp': 60000, 'identityguard.webp': 100000}
        for filename, limit in budgets.items():
            with self.subTest(asset=filename):
                self.assertLess((ROOT / 'assets' / filename).stat().st_size, limit)


if __name__ == '__main__':
    unittest.main(verbosity=2)
