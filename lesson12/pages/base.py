from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://demo.opencart.com/admin/"

    def find_element(self, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                             message=f"Can't find element by locator {locator}")
            return element
        except TimeoutException:
            raise AssertionError('Cant find element by locator')

    def find_elements(self, locator, time=10):
        try:
            elements = WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                              message=f"Can't find elements by locator {locator}")
            return elements
        except TimeoutException:
            raise AssertionError('Cant find elements by locator')

    def go_to(self):
        return self.driver.get(self.base_url)
