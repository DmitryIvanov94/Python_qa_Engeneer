from lesson12.pages.admin_products_page import AdminPageProducts
from lesson12.pages.admin_login_page import AdminLoginPage
from selenium import webdriver
import pytest


@pytest.fixture()
def browser():
    driver = webdriver.Chrome("drivers/chromedriver")
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def admin_page(browser):
    page = AdminLoginPage(browser)
    page.go_to()
    return page


@pytest.fixture()
def admin_page_products(browser):
    page = AdminPageProducts(browser)
    return page
