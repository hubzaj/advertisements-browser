from seleniumwire import webdriver
from seleniumwire.webdriver import Chrome

from browser.browser import Browser
from browser.browser_type import BrowserType


def create_browser(browser_type: BrowserType = BrowserType.CHROME) -> Browser:
    match browser_type:
        case BrowserType.CHROME:
            options: webdriver.ChromeOptions = webdriver.ChromeOptions()
            # options.binary_location = ChromeDriverManager().install()
            driver: Chrome = webdriver.Chrome(options=options)
            driver.maximize_window()
            return Browser(driver)
        case BrowserType.CHROME_HEADLESS:
            options: webdriver.ChromeOptions = webdriver.ChromeOptions()
            options.headless = True
            # options.binary_location = ChromeDriverManager().install()
            driver: Chrome = webdriver.Chrome(options=options)
            driver.maximize_window()
            return Browser(driver)
