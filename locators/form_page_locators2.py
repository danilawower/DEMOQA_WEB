from selenium.webdriver.common.by import By


class FormPageLocators:
    NAME_FIELD = (By.XPATH, "//input[@id='firstName']")
    LASTNAME_FIELD = (By.XPATH, "//input[@id='lastName']")
    EMAIL_FIELD = (By.XPATH, "//input[@id='userEmail']")
    GENDER_RADIO = (By.XPATH, "//label[contains(@for,'gender-radio')]")
    MOBILE_FIELD = (By.XPATH, "//input[@id='userNumber']")
    DATE_FIELD = (By.XPATH, "//input[@id='dateOfBirthInput']")
    DATE_PICK = (By.XPATH, "//div[@class='react-datepicker__week']")
    SUBJECTS = (By.CSS_SELECTOR, "input[id='subjectsInput']")

