from selenium.webdriver.remote.webdriver import WebDriver
from seleniumwire.inspect import InspectRequestsMixin
from seleniumwire.request import Request


class Browser:

    def __init__(self, driver: WebDriver | InspectRequestsMixin):
        self.driver: WebDriver | InspectRequestsMixin = driver

    def open_page(self, url: str, requests_paths_to_wait: list[str] = None) -> list[Request]:
        self.driver.get(url)
        return self.get_network_traffic(requests_paths_to_wait)

    def get_network_traffic(self, requests_paths_to_wait: list[str]) -> list[Request]:
        requests: list[Request] = []
        for request_path_to_wait in requests_paths_to_wait:
            if request := [request for request in self.driver.requests if request_path_to_wait in request.url]:
                requests.append(request[0])
            requests.append(self.driver.wait_for_request(request_path_to_wait, 5))
        return requests

    def close_tab(self):
        self.driver.close()

    def close_browser(self):
        self.driver.quit()
