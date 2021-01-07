from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep


def test_url(browser):
    # Проверка url opencart
    sleep(1)
    assert browser.current_url == "https://demo.opencart.com/"


# 5 тестов для главной страницы c использованием expected_conditions

def test_main_title(browser):
    # Проверка заголовка
    wait = WebDriverWait(browser, 3)
    wait.until(EC.title_is("Your Store"))


def test_main_navbar(browser):
    # Проверка навигационной панели
    wait = WebDriverWait(browser, 3)
    wait.until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='collapse navbar-collapse navbar-ex1-collapse']")))


def test_main_shopping_car_items(browser):
    # Проверка отсутствия элементов в корзине (по тексту)
    wait = WebDriverWait(browser, 3)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div[@class='col-sm-3']/div[@id='cart']/"
                                                           "button[@class='btn btn-inverse btn-block btn-lg dropdown-toggle']/"
                                                           "span[@id='cart-total']"), '0 item(s) - $0.00'))


def test_main_search(browser):
    # Проверка окна поиска (кликабельность)
    wait = WebDriverWait(browser, 3)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@class='col-sm-5']/div[@id='search']/input[@class='form-control input-lg']")))


def test_main_infopanel(browser):
    # Проверка видимости информационной топ панели
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//nav[@id='top']/div[@class='container']")))

# pytest lesson8/test_opencart_main.py
# pytest --options=headless lesson8/test_opencart_main.py
