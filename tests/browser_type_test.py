from unittest import TestCase

from browser_hz.browsers import Browsers


class BrowserTypeTest(TestCase):

    def test_get_supported_browser_type(self) -> None:
        self.assertIsNotNone(Browsers.get_browser("chrome"))

    def test_unsupported_browser_type(self) -> None:
        self.assertRaises(KeyError, lambda: Browsers.get_browser("IE"))
