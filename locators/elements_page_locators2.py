from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    FULL_NAME_FIELD = (By.XPATH, "//input[@id='userName']")
    EMAIL_FIELD = (By.XPATH, "//input[@id='userEmail']")
    CURRENT_ADDRESS_FIELD = (By.XPATH, "//textarea[@id='currentAddress']")
    PERMANENT_ADDRESS_FIELD = (By.XPATH, "//textarea[@id='permanentAddress']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@id='submit']")


class CheckBoxPageLocators:
    CHECKBOX_LIST = (By.XPATH, "//span[@class='rct-checkbox']")
    CHECKBOX_OPEN_BUTTON = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-expand-close']")



class RadioButtonPageLocators:
    YES_BUTTON = (By.XPATH, "//label[@for='yesRadio']")
    IMPRESSIVE_BUTTON = (By.XPATH, "//label[@for='impressiveRadio']")
