def test_login(admin_page):
    """ Проверка входа в аккаунт администратора """

    admin_page.login('demo', 'demo')
    assert admin_page.driver.title == 'Dashboard'


def test_logout(admin_page):
    """ Проверка выхода из аккаунта """

    admin_page.login('demo', 'demo')
    admin_page.logout()
    assert admin_page.driver.title != 'Dashboard'


# Проверка кнопки восстановления пароля
def test_forgot_password(admin_page):
    """ Проверка выхода из аккаунта """

    admin_page.forgot_password()
    assert admin_page.driver.title == 'Forgot Your Password?'
