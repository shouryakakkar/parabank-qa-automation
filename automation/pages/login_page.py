from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BTN = (By.XPATH, "//input[@value='Log In']")
    ERROR_MSG = (By.CLASS_NAME, "error")
    LOGOUT_LINK = (By.LINK_TEXT, "Log Out")

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME).clear()
        self.driver.find_element(*self.USERNAME).send_keys(username)

        self.driver.find_element(*self.PASSWORD).clear()
        self.driver.find_element(*self.PASSWORD).send_keys(password)

        self.driver.find_element(*self.LOGIN_BTN).click()

    def wait_for_login_success(self):
        self.wait.until(
            EC.presence_of_element_located(self.LOGOUT_LINK)
        )

    def wait_for_login_error(self):
        self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MSG)
        )

    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MSG).text
