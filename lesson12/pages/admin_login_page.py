from selenium.webdriver.common.by import By
from .base import BasePage


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

    def _set_username_(self, name):
        self.find_element(locator=self.username).clear()
        self.find_element(locator=self.username).send_keys(name)

    def _set_password_(self, password):
        self.find_element(locator=self.password).clear()
        self.find_element(locator=self.password).send_keys(password)

    def login(self, username, password):
        self._set_username_(username)
        self._set_password_(password)
        self.find_element(locator=self.submit_button).click()

    def logout(self):
        self.find_element(locator=self.logout_button).click()

    def forgot_password(self):
        self.find_element(locator=self.forgotten_pass_button).click()
