import os
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    # Парсер аргументов командной строки
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="https://demo.opencart.com/")
    parser.addoption("--drivers", action="store", default="drivers")
    parser.addoption("--options", action="store", default="")


@pytest.fixture
def browser(request):
    # Сбор параметров запуска для pytest
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    drivers = request.config.getoption("--drivers")
    options = request.config.getoption("--options")

    # Выбор драйвера и опций запуска
    if browser == "chrome":
        chrome_options = webdriver.ChromeOptions()
        if options == "headless":
            chrome_options.add_argument("headless")
        driver = webdriver.Chrome(executable_path=drivers + "//chromedriver.exe", options=chrome_options)

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
    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver

