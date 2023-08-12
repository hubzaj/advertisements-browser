from contextlib import contextmanager
from logging import Logger, getLogger

from browser.browser import Browser
from browser.browser_factory import create_browser
from browser.browser_type import BrowserType

LOGGER: Logger = getLogger(__name__)


@contextmanager
def open_browser(browser_type_: BrowserType) -> Browser:
    browser_: Browser | None = None
    try:
        LOGGER.info(f'Open web browser [{browser_type_}]')
        browser_ = create_browser(browser_type_)
        yield browser_
    finally:
        browser_.close_tab()
        browser_.close_browser()
