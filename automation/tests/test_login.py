from pages.login_page import LoginPage

def test_valid_login(driver):
    login = LoginPage(driver)
    login.login("shourya", "Qwerty!23")

    login.wait_for_login_success()
    assert "Log Out" in driver.page_source


def test_invalid_login(driver):
    login = LoginPage(driver)
    login.login("wrong", "wrong")

    login.wait_for_login_error()
    assert "could not be verified" in login.get_error_message().lower()
