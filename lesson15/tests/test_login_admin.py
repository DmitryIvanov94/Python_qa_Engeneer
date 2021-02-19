from time import sleep
import allure


@allure.feature('Login')
@allure.story('Valid credentials')
@allure.title('Successful login to the administrator account')
def test_login(admin_page):
    sleep(5)
    admin_page.login('demo', 'demo')
    assert admin_page.driver.title == 'Dashboard'


@allure.feature('Login')
@allure.story('Button operation')
@allure.title('Successful logout from the administrator account')
def test_logout(admin_page):
    admin_page.login('demo', 'demo')
    admin_page.logout()
    assert admin_page.driver.title != 'Dashboard'


@allure.feature('Login')
@allure.story('Button operation')
@allure.title('Successful check button Forgot Your Password')
def test_forgot_password(admin_page):
    admin_page.forgot_password()
    assert admin_page.driver.title == 'Forgot Your Password?'
