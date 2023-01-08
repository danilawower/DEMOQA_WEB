from selenium.webdriver.common.by import By

class TextBoxPageLocators:

    #поля которые заполнить и кнопку нажать

    FULL_NAME = (By.XPATH, "//input[@id='userName']")   #по хпасу
    EMAIL = (By.CSS_SELECTOR,  "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR,  "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    #поля которые чекнуть на создание
    CREATED_FULL_NAME = (By.XPATH, "//p[@id='name']")
    CREATED_EMAIL = (By.XPATH, "//p[@id='email']")
    CREATED_CURRENT_ADDRESS = (By.XPATH, "//p[@id='currentAddress']")
    CREATED_PERMANENT_ADDRESS = (By.XPATH, "//p[@id='permanentAddress']")



class CheckBoxPageLocators:

    EXPAND_ALL_BUTTON = (By.XPATH, "//button[@title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")  #несколько элементов  со сходжим селектором или хпасом
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = (".//ancestor::span[@class='rct-text']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class RadioButtonPageLocators:

    YES_RADIOBUTTON = (By.XPATH, "//label[normalize-space()='Yes']")
    IMPRESSIVE_RADIOBUTTON = (By.XPATH, "//label[normalize-space()='Impressive']")
    NO_RADIOBUTTON = (By.XPATH, "//label[normalize-space()='No']")
    OUTPUT_RESULT = (By.XPATH, "//span[@class='text-success']")


class WebTablePageLocators:
    ADD_BUTTON = (By.XPATH, "//button[@id='addNewRecordButton']")
    FIRSTNAME_INPUT = (By.XPATH, "//input[@id='firstName']")
    LASTNAME_INPUT = (By.XPATH, "//input[@id='lastName']")
    EMAIL_INPUT = (By.XPATH, "//input[@id='userEmail']")
    AGE_INPUT = (By.XPATH, "//input[@id='age']")
    SALARY_INPUT = (By.XPATH, "//input[@id='salary']")
    DEPARTMENT_INPUT = (By.XPATH, "//input[@id='department']")
    SUBMIT = (By.XPATH, "//button[@id='submit']")
