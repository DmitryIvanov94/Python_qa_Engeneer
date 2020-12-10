from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep


# 5 тестов для товара "Samsung Galaxy Tab 10.1"

def test_product_page(browser):
    # Проверка нахождения на странице товара
    browser.get(browser.url + "index.php?route=product/product&path=57&product_id=49")
    wait = WebDriverWait(browser, 2)
    wait.until(EC.url_to_be("https://demo.opencart.com/index.php?route=product/product&path=57&product_id=49"))


def test_product_name(browser):
    # Проверка отображения названия товара
    browser.get(browser.url + "index.php?route=product/product&path=57&product_id=49")
    wait = WebDriverWait(browser, 2)
    wait.until(EC.url_to_be("https://demo.opencart.com/index.php?route=product/product&path=57&product_id=49"))

    assert browser.find_element_by_xpath("//div[@id='content']/div[@class='row']/div[@class='col-sm-4']/h1").text == 'Samsung Galaxy Tab 10.1'


def test_product_price(browser):
    # Проверка отображения цены товара
    browser.get(browser.url + "index.php?route=product/product&path=57&product_id=49")
    wait = WebDriverWait(browser, 2)
    wait.until(EC.url_to_be("https://demo.opencart.com/index.php?route=product/product&path=57&product_id=49"))

    assert len(browser.find_element_by_xpath("//div[@class='col-sm-4']/ul[@class='list-unstyled'][2]/li[1]/h2").text) > 1


def test_product_description(browser):
    # Проверка отображения описания товара
    browser.get(browser.url + "index.php?route=product/product&path=57&product_id=49")
    wait = WebDriverWait(browser, 2)
    wait.until(EC.url_to_be("https://demo.opencart.com/index.php?route=product/product&path=57&product_id=49"))

    assert len(browser.find_element_by_xpath("//div[@class='tab-content']/div[@id='tab-description']/p[1]").text) > 50


def test_product_add_to_cart(browser):
    # Проверка кнопки добавления товара в корзину
    browser.get(browser.url + "index.php?route=product/product&path=57&product_id=49")
    wait = WebDriverWait(browser, 2)
    wait.until(EC.url_to_be("https://demo.opencart.com/index.php?route=product/product&path=57&product_id=49"))

    button_add_to_cart = browser.find_element_by_xpath("//div[@class='col-sm-4']/div[@id='product']/div[@class='form-group']/button[@id='button-cart']")
    button_add_to_cart.click()

    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-success alert-dismissible']")))
    sleep(1)
    assert 'Success: You have added Samsung Galaxy Tab 10.1' in browser.find_element_by_xpath(
        "//div[@class='alert alert-success alert-dismissible']").text

# pytest lesson8/test_opencart_product.py
