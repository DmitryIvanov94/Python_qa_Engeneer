from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep


# 5 тестов для страницы каталога Desktops

def test_catalog_page(browser):
    # Проверка нахождения на странице каталога
    browser.get(browser.url + "index.php?route=product/category&path=20")
    wait = WebDriverWait(browser, 2)
    wait.until(EC.url_to_be("https://demo.opencart.com/index.php?route=product/category&path=20"))


def test_catalog_content(browser):
    # Проверка раскрыт ли список с содержимым каталога
    browser.get(browser.url + "index.php?route=product/category&path=20")
    wait = WebDriverWait(browser, 2)
    wait.until(EC.url_to_be("https://demo.opencart.com/index.php?route=product/category&path=20"))

    wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='list-group']/a[@class='list-group-item'][1]")))
    wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='list-group']/a[@class='list-group-item'][2]")))


def test_catalog_list(browser):
    # Проверка выбора вида товаров "список"
    browser.get(browser.url + "index.php?route=product/category&path=20")
    wait = WebDriverWait(browser, 2)
    wait.until(EC.url_to_be("https://demo.opencart.com/index.php?route=product/category&path=20"))

    list = browser.find_element_by_xpath("//div[@class='btn-group btn-group-sm']/button[@id='list-view']")
    list.click()
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//div[@class='btn-group btn-group-sm']/button[@id='list-view']/i[@class='fa fa-th-list']")))


def test_catalog_sort_by(browser):
    # Проверка выбора варианта из выпадающего списка "SortBy:"
    browser.get(browser.url + "index.php?route=product/category&path=20")
    wait = WebDriverWait(browser, 2)
    wait.until(EC.url_to_be("https://demo.opencart.com/index.php?route=product/category&path=20"))

    sort_by_list = browser.find_elements_by_xpath(
        "//div[@class='form-group input-group input-group-sm']/select[@id='input-sort']/option")
    sort_by_list[3].click()
    sleep(1)
    assert browser.find_elements_by_xpath(
        "//div[@class='form-group input-group input-group-sm']/select[@id='input-sort']/option")[
               3].text == 'Price (Low > High)'


def test_catalog_show(browser):
    # Проверка выбора варианта из выпадающего списка "Show"
    browser.get(browser.url + "index.php?route=product/category&path=20")
    wait = WebDriverWait(browser, 2)
    wait.until(EC.url_to_be("https://demo.opencart.com/index.php?route=product/category&path=20"))

    show_list = browser.find_elements_by_xpath(
        "//div[@class='form-group input-group input-group-sm']/select[@id='input-limit']/option")
    show_list[3].click()
    sleep(1)
    assert browser.find_elements_by_xpath(
        "//div[@class='form-group input-group input-group-sm']/select[@id='input-limit']/option")[3].text == '75'

# pytest lesson8/test_opencart_catalog.py
