from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # поля которые заполнить и кнопку нажать

    FULL_NAME = (By.XPATH, "//input[@id='userName']")  # по хпасу
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    # поля которые чекнуть на создание
    CREATED_FULL_NAME = (By.XPATH, "//p[@id='name']")
    CREATED_EMAIL = (By.XPATH, "//p[@id='email']")
    CREATED_CURRENT_ADDRESS = (By.XPATH, "//p[@id='currentAddress']")
    CREATED_PERMANENT_ADDRESS = (By.XPATH, "//p[@id='permanentAddress']")


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.XPATH, "//button[@title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")  # несколько элементов  со сходжим селектором или хпасом
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = (".//ancestor::span[@class='rct-text']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class RadioButtonPageLocators:
    YES_RADIOBUTTON = (By.XPATH, "//label[normalize-space()='Yes']")
    IMPRESSIVE_RADIOBUTTON = (By.XPATH, "//label[normalize-space()='Impressive']")
    NO_RADIOBUTTON = (By.XPATH, "//label[normalize-space()='No']")
    OUTPUT_RESULT = (By.XPATH, "//span[@class='text-success']")


class WebTablePageLocators:
    # add_person
    ADD_BUTTON = (By.XPATH, "//button[@id='addNewRecordButton']")
    FIRSTNAME_INPUT = (By.XPATH, "//input[@id='firstName']")
    LASTNAME_INPUT = (By.XPATH, "//input[@id='lastName']")
    EMAIL_INPUT = (By.XPATH, "//input[@id='userEmail']")
    AGE_INPUT = (By.XPATH, "//input[@id='age']")
    SALARY_INPUT = (By.XPATH, "//input[@id='salary']")
    DEPARTMENT_INPUT = (By.XPATH, "//input[@id='department']")
    SUBMIT = (By.XPATH, "//button[@id='submit']")

    # tables
    FULL_PEOPLE_LIST = (By.XPATH, "//div[@class='rt-tr-group']")
    SEARCH_INPUT = (By.XPATH, "//input[@id='searchBox']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
    ROW_PARENT = ".//ancestor::span[@class='rt-tr-group']"

    # update
    UPDATE_BUTTON = (By.XPATH, "//span[@id='edit-record-1']")


class ButtonsPageLocators:
    DOUBLE_BUTTON = (By.XPATH, "//button[@id='doubleClickBtn']")
    RIGHT_CLICK_BUTTON = (By.XPATH, "//button[@id='rightClickBtn']")
    CLICK_ME_BUTTON = (By.XPATH, "//button[@class='btn btn-primary'][text()='Click Me']")

    # result
    SUCCESS_DOUBLE = (By.XPATH, "//p[@id='doubleClickMessage']")
    SUCCESS_RIGHT = (By.XPATH, "//p[@id='rightClickMessage']")
    SUCCESS_CLICK_ME = (By.XPATH, "//p[@id='dynamicClickMessage']")


class LinksPageLocators:
    SIMPLE_LINK = (By.XPATH, "//a[@id='simpleLink']")
    BAD_REQUEST = (By.XPATH, "//a[@id='bad-request']")


class UploadAndDownloadPageLocators:
    UPLOAD_FILE = (By.XPATH, "//input[@id='uploadFile']")
    UPLOADED_FILE = (By.XPATH, "//p[@id='uploadedFilePath']")
    DOWNLOAD_FILE = (By.XPATH, "//a[@id='downloadButton']")


class DynamicPropertiesPageLocators:
    COLOR_CHANGE_BUTTON = (By.XPATH, "//button[@id='colorChange']")
    VISIBLE_AFTER_FIVE_SEC_BUTTON = (By.XPATH, "//button[@id='visibleAfter']")
    ENABLE_BUTTON = (By.XPATH, "//button[@id='enableAfter']")