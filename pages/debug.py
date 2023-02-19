
from selenium import webdriver

import time

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "C:\\Users\daniil\\PycharmProjects\\automation_qa_course\\downloads"}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver.get('https://samplelib.com/ru/sample-mp4.html')
download = driver.find_element(By.XPATH, "//div[@class='items']//div[1]//div[1]//div[4]//a[1]")
download.click()
time.sleep(5)
driver.close()

#@pytest.fixture(scope="function")
#def driver():
    #driver = webdriver.Chrome(ChromeDriverManager().install())
   # driver.maximize_window()
    #yield driver
    #driver.quit()
