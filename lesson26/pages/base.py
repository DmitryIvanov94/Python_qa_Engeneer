from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
import allure


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://demo.opencart.com/admin/"

    @allure.step("I find element by locator {locator}")
    def find_element(self, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                             message=f"Can't find element by locator {locator}")
            return element
        except TimeoutException:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)

            raise AssertionError('Cant find element by locator')

    @allure.step("I find elements by locator {locator}")
    def find_elements(self, locator, time=10):
        try:
            elements = WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                              message=f"Can't find elements by locator {locator}")
            return elements
        except TimeoutException:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)

            raise AssertionError('Cant find elements by locator')

    @allure.step("I go to base url")
    def go_to(self):
        return self.driver.get(self.base_url)
