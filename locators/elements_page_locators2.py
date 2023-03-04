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


class WebTablePageLocators:
    ADD_BUTTON = (By.XPATH, "//button[@id='addNewRecordButton']")
    FIRST_NAME = (By.XPATH, "//input[@id='firstName']")
    LAST_NAME = (By.XPATH, "//input[@id='lastName']")
    EMAIL = (By.XPATH, "//input[@id='userEmail']")
    AGE = (By.XPATH, "//input[@id='age']")
    SALARY = (By.XPATH, "//input[@id='salary']")
    DEPARTMENT = (By.XPATH, "//input[@id='department']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@id='submit']")
    INPUT_SEARCH = (By.XPATH, "//input[@id='searchBox']")
    TABLE_NAME = (By.XPATH, "//div[@class='rt-tr -odd']")


class ButtonPageLocators:
    DOUBLE_CLICK = (By.XPATH, "//button[@id='doubleClickBtn']")
    RIGHT_CLICK = (By.XPATH, "//button[@id='rightClickBtn']")
    CLICK_ME = (By.XPATH, "//button[@type='button'][text()='Click Me']")


class LinksPageLocators:
    HOME_LINK = (By.XPATH, "//a[@id='simpleLink']")
    DYNAMIC_LINK = (By.XPATH, "//a[@id='dynamicLink']")
    FORBIDDEN_LINK = (By.XPATH, "//a[@id='forbidden']")


class UploadDownloadPageLocators:
    DOWNLOAD_BUTTON = (By.XPATH, "//a[@id='downloadButton']")
    UPLOAD_BUTTON = (By.XPATH, "//input[@id='uploadFile']")


class DynamicPropertiesPageLocators:
    ENABLE_AFTER_BUTTON = (By.XPATH, "//button[@id='enableAfter']")
    COLOR_CHANGE_BUTTON = (By.XPATH, "//button[@id='colorChange']")
    VISIBLE_AFTER_BUTTON = (By.XPATH, "//button[@id='visibleAfter']")