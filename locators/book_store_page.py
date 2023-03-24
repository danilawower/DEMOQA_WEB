from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FIELD = (By.XPATH, "//input[@id='userName']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@id='login']")
    NEW_USER_BUTTON = (By.XPATH, "//button[@id='newUser']")
    