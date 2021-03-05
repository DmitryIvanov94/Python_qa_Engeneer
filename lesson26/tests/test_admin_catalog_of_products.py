import allure


@allure.feature('Catalog')
@allure.story('Products')
@allure.title('Check product name')
def test_catalog_check_product_name(admin_page, admin_page_products):
    admin_page.login('demo', 'demo')
    admin_page_products.open_catalog()
    admin_page_products.open_products()
    assert len(admin_page_products.product_name()) > 0


@allure.feature('Catalog')
@allure.story('Products')
@allure.title('Check product model')
def test_catalog_check_product_model(admin_page, admin_page_products):
    admin_page.login('demo', 'demo')
    admin_page_products.open_catalog()
    admin_page_products.open_products()
    assert len(admin_page_products.product_model()) > 0


@allure.feature('Catalog')
@allure.story('Products')
@allure.title('Check product price')
def test_catalog_check_product_price(admin_page, admin_page_products):
    admin_page.login('demo', 'demo')
    admin_page_products.open_catalog()
    admin_page_products.open_products()
    assert len(admin_page_products.product_price()) > 0
