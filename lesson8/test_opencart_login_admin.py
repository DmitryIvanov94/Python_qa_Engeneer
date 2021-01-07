from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep


# 5 тестов для страницы логина в админку

def test_login_admin_page(browser):
    # Проверка нахождения на странице логина в админку
    browser.get(browser.url + "admin")
    wait = WebDriverWait(browser, 2)
    wait.until(EC.url_to_be("https://demo.opencart.com/admin/"))


def test_login_admin_correct(browser):
    # Проверка входа с заполненными данными
    browser.get(browser.url + "admin")
    wait = WebDriverWait(browser, 2)
    wait.until(EC.url_to_be("https://demo.opencart.com/admin/"))

    submit_button = browser.find_element_by_xpath("//button[@class='btn btn-primary']")
    submit_button.click()
    sleep(1)

    wait.until(EC.url_contains("https://demo.opencart.com/admin/index.php?route=common/"))
    assert browser.find_element_by_xpath("//div[@class='container-fluid']/h1").text == 'Dashboard'


def test_login_admin_add_password(browser):
    # Проверка ввода пароля
    browser.get(browser.url + "admin")
    wait = WebDriverWait(browser, 2)
    wait.until(EC.url_to_be("https://demo.opencart.com/admin/"))

    password = browser.find_element_by_xpath(
        "//div[@class='form-group'][2]/div[@class='input-group']/input[@id='input-password']")
    password.clear()
    password.send_keys('DemoVasia12345')
    sleep(1)

    assert browser.find_element_by_xpath(
        "//div[@class='form-group'][2]/div[@class='input-group']/input[@id='input-password']").get_attribute(
        "value") == 'DemoVasia12345'


def test_login_admin_add_username(browser):
    # Проверка ввода имени пользователя
    browser.get(browser.url + "admin")
    wait = WebDriverWait(browser, 2)
    wait.until(EC.url_to_be("https://demo.opencart.com/admin/"))

    username = browser.find_element_by_xpath(
        "//div[@class='form-group'][1]/div[@class='input-group']/input[@id='input-username']")
    username.clear()
    username.send_keys('demoVasia')
    sleep(1)

    assert browser.find_element_by_xpath(
        "//div[@class='form-group'][1]/div[@class='input-group']/input[@id='input-username']").get_attribute(
        "value") == 'demoVasia'


def test_login_admin_forgot_password(browser):
    # Проверка кнопки "Forgotten Password"
    browser.get(browser.url + "admin")
    wait = WebDriverWait(browser, 2)
    wait.until(EC.url_to_be("https://demo.opencart.com/admin/"))

    forgoten_pass_button = browser.find_element_by_xpath(
        "//div[@class='panel-body']/form/div[@class='form-group'][2]/span[@class='help-block']/a")
    forgoten_pass_button.click()
    sleep(1)

    wait.until(EC.url_to_be("https://demo.opencart.com/admin/index.php?route=common/forgotten"))
    assert browser.find_element_by_xpath(
        "//div[@class='panel-heading']/h1[@class='panel-title']").text == 'Forgot Your Password?'


# 2 тестовых сценария на раздел администратора

def test_login_admin_and_logout(browser):
    # Проверка разлогина
    browser.get(browser.url + "admin")
    wait = WebDriverWait(browser, 2)
    wait.until(EC.url_to_be("https://demo.opencart.com/admin/"))

    submit_button = browser.find_element_by_xpath("//button[@class='btn btn-primary']")
    submit_button.click()
    wait.until(EC.url_contains("https://demo.opencart.com/admin/index.php?route=common/"))
    sleep(1)

    logout_button = browser.find_element_by_xpath("//ul[@class='nav navbar-nav navbar-right']/li[2]/a")
    logout_button.click()
    wait.until(EC.url_contains("https://demo.opencart.com/admin/index.php?route=common/login"))


def test_login_admin_catalog_products(browser):
    # Проверка перехода к разделу с товарами и талицы товаров
    browser.get(browser.url + "admin")
    wait = WebDriverWait(browser, 2)
    wait.until(EC.url_to_be("https://demo.opencart.com/admin/"))

    submit_button = browser.find_element_by_xpath("//button[@class='btn btn-primary']")
    submit_button.click()
    wait.until(EC.url_contains("https://demo.opencart.com/admin/index.php?route=common/"))
    sleep(1)

    catalog = browser.find_element_by_xpath("//li[@id='menu-catalog']/a[@class='parent collapsed']")
    catalog.click()
    sleep(1)

    products = browser.find_element_by_xpath("//li[@id='menu-catalog']/ul[@id='collapse1']/li[2]/a")
    products.click()
    sleep(1)

    # Существует ли таблица и есть ли название хотя бы у одного товара
    wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='panel panel-default']/div[@class='panel-body']")))
    product_1_name = browser.find_element_by_xpath(
        "//form[@id='form-product']/div[@class='table-responsive']/table[@class='table table-bordered table-hover']/tbody/tr[1]/td[@class='text-left'][1]").text
    assert len(product_1_name) > 0

# pytest lesson8/test_opencart_login_admin.py
