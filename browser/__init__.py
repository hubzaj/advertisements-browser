from contextlib import contextmanager

from browser.browser import Browser
from browser.browser_factory import create_browser
from browser.browser_type import BrowserType


@contextmanager
def open_browser(browser_type_: BrowserType) -> Browser:
    browser_: Browser | None = None
    try:
        browser_ = create_browser(browser_type_)
        yield browser_
    finally:
        browser_.close_tab()
        browser_.close_browser()
