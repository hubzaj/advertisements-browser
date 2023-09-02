from unittest import TestCase

from browser_hz.browser_type import BrowserType


class BrowserTypeTest(TestCase):

    def test_get_supported_browser_type(self) -> None:
        self.assertIsNotNone(BrowserType.get_browser("chrome"))

    def test_unsupported_browser_type(self) -> None:
        self.assertRaises(KeyError, lambda: BrowserType.get_browser("IE"))
