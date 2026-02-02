from pages.login_page import LoginPage
from pages.open_account_page import OpenAccountPage
from pages.transfer_funds_page import TransferFundsPage

def test_transfer_funds(driver):
    # login
    login = LoginPage(driver)
    login.login("shourya", "Qwerty!23")
    login.wait_for_login_success()

    # ensure second account exists
    open_account = OpenAccountPage(driver)
    open_account.open_new_account("SAVINGS")
    assert open_account.is_account_opened()

    # transfer funds
    transfer = TransferFundsPage(driver)
    transfer.transfer_funds("25")

    assert transfer.is_transfer_successful()
