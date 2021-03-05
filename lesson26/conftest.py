from .pages.admin_login_page import AdminLoginPage
from .pages.admin_products_page import AdminPageProducts
from selenium import webdriver
import requests
import allure
import pytest
import json


@pytest.fixture()
def admin_page(browser):
    page = AdminLoginPage(browser)
    page.go_to()
    return page


@pytest.fixture()
def admin_page_products(browser):
    page = AdminPageProducts(browser)
    return page


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="https://demo.opencart.com/admin/")
    parser.addoption("--drivers", action="store", default="drivers")
    parser.addoption("--options", action="store", default="")
    parser.addoption("--executor", default="192.168.0.102")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    drivers = request.config.getoption("--drivers")
    executor = request.config.getoption("--executor")

    driver = webdriver.Remote(
        command_executor="http://{}:4444/wd/hub".format(executor),
        desired_capabilities={"browserName": browser, "enableVNC": True, "screenResolution": "1920x1080"})

    driver.maximize_window()

    def finish():
        driver.quit()
        requests.delete(f"http://{executor}:4444/wd/hub/session/{driver.session_id}", verify=False)

    allure.attach(body=json.dumps(driver.capabilities), attachment_type=allure.attachment_type.JSON)
    request.addfinalizer(finish)
    return driver
