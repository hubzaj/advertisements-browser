from contextlib import contextmanager

from selenium.webdriver.remote.webdriver import WebDriver

from .browser_factory import create_browser
from .browser_type import BrowserType


@contextmanager
def open_browser(browser: BrowserType) -> WebDriver:
    driver = None
    try:
        driver = create_browser(browser)
        yield driver
    finally:
        driver.close()
        driver.quit()
