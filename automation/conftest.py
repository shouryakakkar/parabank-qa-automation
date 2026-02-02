import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
@pytest.fixture(scope="function")
def driver():
    options = Options()
    # options.add_argument("--headless=new")  # ❌ comment this out
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get("http://localhost:8080/parabank")
    driver.implicitly_wait(2)

    yield driver
    driver.quit()
