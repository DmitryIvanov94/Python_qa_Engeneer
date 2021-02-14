from time import sleep
from selenium.webdriver.common.by import By
from .base import BasePage


class AdminPageProducts(BasePage):
    catalog = (By.XPATH, "//li[@id='menu-catalog']/a[@class='parent collapsed']")
    products = (By.XPATH, "//li[@id='menu-catalog']/ul[@id='collapse1']/li[2]/a")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.number_product = 1
        self.number_model = 1
        self.number_price = 1

    def open_catalog(self):
        self.find_element(locator=self.catalog).click()
        sleep(1)

    def open_products(self):
        self.find_element(locator=self.products).click()

    def product_name(self):
        name = (By.XPATH,
                "//form[@id='form-product']/div[@class='table-responsive']/table[@class='table table-bordered "
                "table-hover']/tbody/tr[{}]/td[@class='text-left'][1]".format(self.number_product))
        return name

    def product_model(self):
        model = (By.XPATH,
                 "//form[@id='form-product']/div[@class='table-responsive']/table[@class='table table-bordered "
                 "table-hover']/tbody/tr[{}]/td[@class='text-left'][2]".format(self.number_model))
        return model

    def product_price(self):
        price = (By.XPATH,
                 "//form[@id='form-product']/div[@class='table-responsive']/table[@class='table table-bordered "
                 "table-hover']/tbody/tr[{}]/td[@class='text-right'][1]".format(self.number_price))
        return price
