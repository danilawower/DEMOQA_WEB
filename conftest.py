import datetime
from datetime import datetime

import allure
import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager




@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f'Screenshot {datetime.today()}', attachment_type=allure.attachment_type.PNG)
    driver.quit()


#@pytest.fixture(scope="function")
#def driver():
    #chrome_options = webdriver.ChromeOptions()
    #driver = webdriver.Remote(
        #command_executor='http://selenoid:4444/wd/hub',
        #desired_capabilities={'browserName': 'chrome',
                              #'version': '92.0'},
        #options=chrome_options)
    #driver.maximize_window()
    #yield driver
    #driver.quit()