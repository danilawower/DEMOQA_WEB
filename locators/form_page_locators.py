import random

from selenium.webdriver.common.by import By


class FormPageLocators:
    FIRST_NAME = (By.XPATH, "//input[@id='firstName']")
    LAST_NAME = (By.XPATH, "//input[@id='lastName']")
    EMAIL = (By.XPATH, "//input[@id='userEmail']")
    GENDER = (By.CSS_SELECTOR, f"div[class*='custom-control'] label[for='gender-radio-{random.randint(1,3)}']") #f содержит выражение внутри скобок(строка)
    MOBILE = (By.XPATH, "//input[@id='userNumber']")
    DATE_OF_BIRTH = (By.XPATH, "//input[@id='dateOfBirthInput']")
    SUBJECT = (By.CSS_SELECTOR, "input[id='subjectsInput']")
    HOBBIES = (By.CSS_SELECTOR, f"div[class*='custom-control'] label[for='hobbies-checkbox-{random.randint(1,3)}']")
    FILE_INPUT = (By.XPATH, "//input[@id='uploadPicture']")
    CURRENT_ADDRESS = (By.XPATH, "//textarea[@id='currentAddress']")
    SELECT_STATE = (By.XPATH, "//div[contains(text(),'Select State')]")
    STATE_INPUT = (By.CSS_SELECTOR, "input[id='react-select-3-input']")
    SELECT_CITY = (By.XPATH, "//div[@id='city']")
    CITY_INPUT = (By.CSS_SELECTOR, "input[id='react-select-4-input']")
    SUBMIT = (By.XPATH, "//button[@id='submit']")


    #table results

    RESULT_TABLE = (By.XPATH, "//div[@class='table-responsive']//td[2]") #у нужных полей индексы td2. он возьмёт каждый
