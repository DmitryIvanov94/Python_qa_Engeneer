# Переход к разделу с товарами, проверка названия товара
def test_catalog_check_product_name(admin_page, admin_page_products):
    admin_page.login('demo', 'demo')
    admin_page_products.open_catalog()
    admin_page_products.open_products()
    assert len(admin_page_products.product_name()) > 0


# Переход к разделу с товарами, проверка модели товара
def test_catalog_check_product_model(admin_page, admin_page_products):
    admin_page.login('demo', 'demo')
    admin_page_products.open_catalog()
    admin_page_products.open_products()
    assert len(admin_page_products.product_model()) > 0


# Переход к разделу с товарами, проверка цены товара
def test_catalog_check_product_price(admin_page, admin_page_products):
    admin_page.login('demo', 'demo')
    admin_page_products.open_catalog()
    admin_page_products.open_products()
    assert len(admin_page_products.product_price()) > 0
