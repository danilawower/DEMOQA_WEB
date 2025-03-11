import datetime
from datetime import datetime
import allure
import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager



@pytest.fixture(scope='session')
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-cache")
    driver = webdriver.Chrome()
    driver.maximize_window()
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f'Screenshot {datetime.today()}', attachment_type=allure.attachment_type.PNG)
    yield driver
    driver.close()
    driver.quit()



