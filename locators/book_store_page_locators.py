from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FIELD = (By.XPATH, "//input[@id='userName']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@id='login']")
    NEW_USER_BUTTON = (By.XPATH, "//button[@id='newUser']")
    FIRST_NAME = (By.XPATH, "//input[@id='firstname']")
    LAST_NAME = (By.XPATH, "//input[@id='lastname']")
    CAPTCHA_CHECKBOX = (By.XPATH, "//span[@role='checkbox']")
    REGISTER_BUTTON = (By.XPATH, "//button[@id='register']")
    GO_TO_STORE_BUTTON = (By.XPATH, "//button[@id='gotoStore']")
    BOOK_LIST = (By.XPATH, "//span[@class='mr-2']")
    ADD_NEW_BOOK = (By.XPATH, "//button[@id='addNewRecordButton'][text()='Add To Your Collection']")
    DELETE_BOOK = (By.XPATH, "//div[@class='text-right button di']//button[@id='submit']")
    MY_BOOKS = (By.XPATH, "//span[@class='mr-2']")
    SEARCH_BOX = (By.XPATH, "//input[@id='searchBox']")