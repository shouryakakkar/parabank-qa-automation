from pages.login_page import LoginPage
from pages.open_account_page import OpenAccountPage

def test_open_new_account(driver):
    login = LoginPage(driver)
    login.login("shourya", "Qwerty!23")
    login.wait_for_login_success()

    open_account = OpenAccountPage(driver)
    open_account.open_new_account("SAVINGS")

    assert open_account.is_account_opened()
