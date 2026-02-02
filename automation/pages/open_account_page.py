from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OpenAccountPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    OPEN_NEW_ACCOUNT_LINK = (By.XPATH, "//a[contains(@href,'openaccount')]")
    ACCOUNT_TYPE = (By.ID, "type")
    OPEN_NEW_ACCOUNT_BTN = (By.XPATH, "//input[@value='Open New Account']")
    SUCCESS_MESSAGE = (By.XPATH, "//h1[contains(text(),'Account Opened')]")
    NEW_ACCOUNT_ID = (By.ID, "newAccountId")
    LOGOUT_LINK = (By.LINK_TEXT, "Log Out")

    def open_new_account(self, account_type="SAVINGS"):
        # ensure user is logged in
        self.wait.until(
            EC.presence_of_element_located(self.LOGOUT_LINK)
        )

        self.wait.until(
            EC.element_to_be_clickable(self.OPEN_NEW_ACCOUNT_LINK)
        ).click()

        select = Select(
            self.wait.until(EC.element_to_be_clickable(self.ACCOUNT_TYPE))
        )
        select.select_by_visible_text(account_type)

        self.wait.until(
            EC.element_to_be_clickable(self.OPEN_NEW_ACCOUNT_BTN)
        ).click()

    def is_account_opened(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        ).is_displayed()

    def get_new_account_id(self):
        return self.wait.until(
            EC.presence_of_element_located(self.NEW_ACCOUNT_ID)
        ).text
