from selenium.webdriver.common.by import By
from .base import BasePage
import allure


class AdminLoginPage(BasePage):
    username = (By.ID, 'input-username')
    password = (By.ID, 'input-password')
    submit_button = (By.CSS_SELECTOR, 'button')
    logout_button = (By.XPATH, "//ul[@class='nav navbar-nav navbar-right']/li[2]/a")
    forgotten_pass_button = (By.XPATH, "//div[@class='panel-body']/form/div[@class='form-group'][2]/span["
                                       "@class='help-block']/a")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("I clear the username field and enter the name {name}")
    def _set_username_(self, name):
        self.find_element(locator=self.username).clear()
        self.find_element(locator=self.username).send_keys(name)

    @allure.step("I clear the password field and enter the password {password}")
    def _set_password_(self, password):
        self.find_element(locator=self.password).clear()
        self.find_element(locator=self.password).send_keys(password)

    @allure.step("I press the login button with the entered data {username}, {password}")
    def login(self, username, password):
        self._set_username_(username)
        self.logger.info("Input username")
        self._set_password_(password)
        self.logger.info("Input password")
        self.find_element(locator=self.submit_button).click()
        self.logger.info("Click submit button")

    @allure.step("I press the logout button")
    def logout(self):
        self.find_element(locator=self.logout_button).click()
        self.logger.info("Click logout button")

    @allure.step("I press the forgot password button")
    def forgot_password(self):
        self.find_element(locator=self.forgotten_pass_button).click()
        self.logger.info("Click forgotten pass button")
