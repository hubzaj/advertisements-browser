from unittest import TestCase

from src.browser_type import BrowserType


class BrowserTypeTest(TestCase):

    def test_get_supported_browser_type(self):
        self.assertIsNotNone(BrowserType.get_browser("chrome"))

    def test_unsupported_browser_type(self):
        self.assertRaises(KeyError, lambda: BrowserType.get_browser("IE"))
