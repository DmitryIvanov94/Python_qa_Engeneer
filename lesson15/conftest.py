from lesson15.pages.admin_products_page import AdminPageProducts
from lesson15.pages.admin_login_page import AdminLoginPage
from selenium import webdriver
import pytest
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - [%(levelname)s] - %(name)s - %(filename)s.%(funcName)s - %(message)s',
                    filename="lesson15/logs/selenium.log")


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
    # parser.addoption("--executor", action="store", default="127.0.0.1")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    drivers = request.config.getoption("--drivers")
    options = request.config.getoption("--options")
    executor = request.config.getoption("--executor")

    logger = logging.getLogger('BrowserLogger')
    test_name = request.node.name
    logger.info("===> Test {} started".format(test_name))
    logger.info("Browser {} started".format(browser))

    if browser == "chrome":
        chrome_options = webdriver.ChromeOptions()
        if options == "headless":
            chrome_options.add_argument("headless")
        driver = webdriver.Chrome(executable_path=drivers + "//chromedriver.exe", options=chrome_options)
        # driver = webdriver.Remote(
        #     command_executor="http://{}:4444/wd/hub".format(executor),
        #     desired_capabilities={"browserName": browser})
        logger.info("Browser {} started with {}".format(browser, driver.desired_capabilities))

    elif browser == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        if options == "headless":
            firefox_options.add_argument("headless")
        driver = webdriver.Firefox(executable_path=drivers + "//geckodriver.exe", options=firefox_options)

    else:
        ie_options = webdriver.IeOptions()
        if options == "headless":
            ie_options.add_argument("headless")
        driver = webdriver.Ie(executable_path=drivers + "//IEDriverServer.exe", options=ie_options)

    driver.maximize_window()

    def finish():
        driver.close()
        logger.info("Browser {} closed".format(browser))
        logger.info("===> Test {} finished\n".format(test_name))

    request.addfinalizer(finish)
    return driver
