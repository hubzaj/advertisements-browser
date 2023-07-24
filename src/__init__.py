from contextlib import contextmanager

from .browser import Browser
from .browser_factory import create_browser
from .browser_type import BrowserType


@contextmanager
def open_browser(browser_type_: BrowserType) -> Browser:
    browser_: Browser | None = None
    try:
        browser_ = create_browser(browser_type_)
        yield browser_
    finally:
        browser_.close_tab()
        browser_.close_browser()
