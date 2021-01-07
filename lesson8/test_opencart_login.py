from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep


# 5 тестов для страницы логина

def test_login_title(browser):
    # Проверка нахождения на странице логина
    browser.get(browser.url + "index.php?route=account/login")
    wait = WebDriverWait(browser, 2)
    wait.until(EC.url_to_be("https://demo.opencart.com/index.php?route=account/login"))


def test_login_add_email(browser):
    # Проверка ввода почты
    browser.get(browser.url + "index.php?route=account/login")
    wait = WebDriverWait(browser, 2)
    wait.until(EC.url_to_be("https://demo.opencart.com/index.php?route=account/login"))

    email = browser.find_element_by_xpath("//div[@class='form-group'][1]/input[@id='input-email']")
    email.send_keys('Vasia12345@yandex.ru')
    sleep(1)
    assert browser.find_element_by_xpath("//div[@class='form-group'][1]/input[@id='input-email']").get_attribute(
        "value") == 'Vasia12345@yandex.ru'


def test_login_add_password(browser):
    # Проверка ввода пароля
    browser.get(browser.url + "index.php?route=account/login")
    wait = WebDriverWait(browser, 2)
    wait.until(EC.url_to_be("https://demo.opencart.com/index.php?route=account/login"))

    password = browser.find_element_by_xpath("//div[@class='form-group'][2]/input[@id='input-password']")
    password.send_keys('SuperVasia12345')
    sleep(1)
    assert browser.find_element_by_xpath("//div[@class='form-group'][2]/input[@id='input-password']").get_attribute(
        "value") == 'SuperVasia12345'


def test_login_no_email_and_pass(browser):
    # Проверка входа без почты
    browser.get(browser.url + "index.php?route=account/login")
    wait = WebDriverWait(browser, 2)
    wait.until(EC.url_to_be("https://demo.opencart.com/index.php?route=account/login"))

    password = browser.find_element_by_xpath("//div[@class='form-group'][2]/input[@id='input-password']")
    password.send_keys('SuperVasia12345')

    login_button = browser.find_element_by_xpath("//form/input[@class='btn btn-primary']")
    login_button.click()

    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//div[@id='account-login']/div[@class='alert alert-danger alert-dismissible']")))
    sleep(1)
    assert browser.find_element_by_xpath(
        "//div[@id='account-login']/div[@class='alert alert-danger alert-dismissible']").text \
           == 'Warning: No match for E-Mail Address and/or Password.'


def test_login_false_email_pass(browser):
    # Проверка входа с неверной связкой логин/пароль
    browser.get(browser.url + "index.php?route=account/login")
    wait = WebDriverWait(browser, 2)
    wait.until(EC.url_to_be("https://demo.opencart.com/index.php?route=account/login"))

    email = browser.find_element_by_xpath("//div[@class='form-group'][1]/input[@id='input-email']")
    email.send_keys('Vasia12345@yandex.ru')
    password = browser.find_element_by_xpath("//div[@class='form-group'][2]/input[@id='input-password']")
    password.send_keys('SuperVasia12345')
    login_button = browser.find_element_by_xpath("//form/input[@class='btn btn-primary']")
    login_button.click()

    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//div[@id='account-login']/div[@class='alert alert-danger alert-dismissible']")))
    sleep(1)
    assert browser.find_element_by_xpath(
        "//div[@id='account-login']/div[@class='alert alert-danger alert-dismissible']").text \
           == 'Warning: No match for E-Mail Address and/or Password.'

# pytest lesson8/test_opencart_login.py
