from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TransferFundsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    TRANSFER_FUNDS_LINK = (By.LINK_TEXT, "Transfer Funds")
    AMOUNT = (By.ID, "amount")
    FROM_ACCOUNT = (By.ID, "fromAccountId")
    TO_ACCOUNT = (By.ID, "toAccountId")
    TRANSFER_BTN = (By.XPATH, "//input[@value='Transfer']")
    SUCCESS_MESSAGE = (By.XPATH, "//h1[contains(text(),'Transfer Complete')]")

    def transfer_funds(self, amount="10"):
        # open transfer funds page
        self.wait.until(
            EC.element_to_be_clickable(self.TRANSFER_FUNDS_LINK)
        ).click()

        # enter amount
        amt = self.wait.until(EC.element_to_be_clickable(self.AMOUNT))
        amt.clear()
        amt.send_keys(amount)

        from_acc = Select(
            self.wait.until(EC.element_to_be_clickable(self.FROM_ACCOUNT))
        )
        to_acc = Select(
            self.wait.until(EC.element_to_be_clickable(self.TO_ACCOUNT))
        )

        # select first two different accounts
        from_acc.select_by_index(0)
        to_acc.select_by_index(1)

        self.wait.until(
            EC.element_to_be_clickable(self.TRANSFER_BTN)
        ).click()

    def is_transfer_successful(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        ).is_displayed()
