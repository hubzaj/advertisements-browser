from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from seleniumwire.inspect import InspectRequestsMixin
from seleniumwire.request import Request


class Browser:

    def __init__(self, driver: WebDriver | InspectRequestsMixin):
        self.driver: WebDriver | InspectRequestsMixin = driver

    def open_page(self, url: str) -> 'Browser':
        self.driver.get(url)
        return self

    def click(self, locator: (By, str)) -> 'Browser':
        self.__wait_for_element_to_be_clickable(locator)
        element_to_be_clicked: WebElement = self.driver.find_element(by=locator[0], value=locator[1])
        element_to_be_clicked.click()
        return self

    def wait_for_requests(self, requests_paths_to_wait: list[str] = None) -> 'Browser':
        self.get_network_traffic(requests_paths_to_wait)
        return self

    def get_network_traffic(self, requests_paths_to_wait: list[str]) -> list[Request]:
        requests: list[Request] = []
        for request_path_to_wait in requests_paths_to_wait:
            if request := [request for request in self.driver.requests if request_path_to_wait in request.url]:
                requests.append(request[0])
            else:
                requests.append(
                    self.driver.wait_for_request(
                        # pat=request_path_to_wait.translate(str.maketrans({'?': r'\?'})),
                        pat=request_path_to_wait,
                        timeout=5
                    )
                )
        return requests

    def close_tab(self) -> 'Browser':
        self.driver.close()
        return self

    def close_browser(self) -> 'Browser':
        self.driver.quit()
        return self

    def close_newly_opened_tab(self) -> 'Browser':
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[1])
        self.close_tab()
        self.driver.switch_to.window(window_handles[0])
        return self

    def __wait_for_element_to_be_clickable(self, locator: (By, str)) -> 'Browser':
        wait: WebDriverWait = WebDriverWait(self.driver, timeout=5)
        wait.until(expected_conditions.element_to_be_clickable(locator))
        return self
