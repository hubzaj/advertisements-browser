from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from .browser_type import BrowserType


def create_browser(browser_type: BrowserType = BrowserType.CHROME) -> WebDriver:
    match browser_type:
        case BrowserType.CHROME:
            driver: WebDriver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
            driver.maximize_window()
            return driver
