from selenium.webdriver.common.by import By


class MainPageLocators:
    START_BUTTON = (By.XPATH, "//button[@id='start']")
    EMAIL_FIELD = (
    By.XPATH, "//input[@formcontrolname='email'][@class='form-control ng-untouched ng-pristine ng-invalid']")
    CHOICE_BUSINESS = (By.XPATH, "//span[text()='Отрасль вашего бизнеса']")
    BUSINESS_LIST = (By.XPATH, "//mat-option[@class='mat-option mat-focus-indicator ng-star-inserted']")
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password'][@placeholder='Пароль']")
    PASSWORD_REPEAT_FIELD = (By.XPATH, "//input[@type='password'][@placeholder='Повторите пароль']")
    ID78 = (By.XPATH, "//mat-option[@id='mat-option-62']")
    CHECKBOX = (By.XPATH, "//span[@class='mat-checkbox-inner-container mat-checkbox-inner-container-no-side-margin']")
    ACCEPT_BUTTON = (By.XPATH, "//form[@class='register ng-dirty ng-touched ng-valid']//button[@id='registerBtn']")
    REGISTRATION_SUCCESS_BUTTON = (By.XPATH, "//button[contains(text(),'Хорошо')]")


class LoginLogoutLocators:
    MY_PROFILE = (By.XPATH, "//lib-max-icon[@class='profile-icon']//*[name()='svg']")
    PROFILE_LOGOUT_BUTTON = (By.XPATH, "//button[@class='log-out-btn ng-star-inserted']")

    START_BUTTON = (By.XPATH, "//button[@id='start']")
    VHOD_BUTTON = (By.XPATH, "//a[@role='tab'][@aria-selected='false'][text()='Вход']")
    EMAIL_FIELD = (By.XPATH, "//form[@class='login ng-untouched ng-pristine ng-invalid']//input[@placeholder='Ваш e-mail']")
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password'][@placeholder='Пароль']")
    LOGIN_BUTTON1 = (By.XPATH, "//button[@id='loginBtn']")


class ProfilePageLocators:
    MY_PROFILE = (By.XPATH, "//lib-max-icon[@class='profile-icon']//*[name()='svg']")
    NAME_FIELD = (By.XPATH, "//input[@id='nameField']")
    PHONE_FIELD = (By.XPATH, "//input[@id='phoneField']")
    EMAIL_PROFILE_FIELD = (By.XPATH, "//input[@id='emailField']")
    SAVE_CHANGES_BUTTON = (By.XPATH, "//button[@class='chat-btn save_btn ng-star-inserted']")

    #login
    START_BUTTON = (By.XPATH, "//button[@id='start']")
    VHOD_BUTTON = (By.XPATH, "//a[@role='tab'][@aria-selected='false'][text()='Вход']")
    EMAIL_FIELD = (By.XPATH, "//form[@class='login ng-untouched ng-pristine ng-invalid']//input[@placeholder='Ваш e-mail']")
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password'][@placeholder='Пароль']")
    LOGIN_BUTTON1 = (By.XPATH, "//button[@id='loginBtn']")


class FirsStepScenarioLocators:
    ZAPUSK_KOMPANII_BUTTON = (By.XPATH, '//p[@class="title"][text()="Запуск первой рекламной кампании"]')
    NEXT_BUTTON = (By.XPATH, "//button[@type='button']")
    NAME_PLACEHOLDER = (By.XPATH, "//input[@placeholder='Поле для ввода имени пользователя']")
    MOBILE_PHONE_BUTTON = (By.XPATH, "//button[@type='button']")
    MOBILE_PHONE_FIELD = (By.XPATH, "//input[@type='text']")
    BRAND_NAME_FIELD = (By.XPATH, "//input[@type='text']")
    COMPANY_NAME_FIELD = (By.XPATH, "//input[@type='text']")
    BUSINESS_TYPE = (By.XPATH, "//mat-checkbox")
    BUSINESS_RADIOBUTTON = (By.XPATH, "//mat-radio-button")
    BUSINESS_CHECKBOX = (By.XPATH, "//mat-checkbox")
    BUSINESS_CHECKBOX2 = (By.XPATH, "//span[@class='mat-checkbox-inner-container']")
    NEXT_BUTTON_WEBSITE = (By.XPATH, "//max-button-message//button")
    WEBSITE_FIELD = (By.XPATH, "//input[@placeholder='Ссылка на веб-сайт']")
    VK_FB_INS = (By.XPATH, "//span[@class='mat-checkbox-inner-container']")
    VK_FIELD = (By.XPATH, "//input[@placeholder='Ваш ВКонтакте']")
    STEP_COUNTER = (By.CSS_SELECTOR, "div[class='progress-bar-container--status']")

    # login
    START_BUTTON = (By.XPATH, "//button[@id='start']")
    VHOD_BUTTON = (By.XPATH, "//a[@role='tab'][@aria-selected='false'][text()='Вход']")
    EMAIL_FIELD = (By.XPATH, "//form[@class='login ng-untouched ng-pristine ng-invalid']//input[@placeholder='Ваш e-mail']")
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password'][@placeholder='Пароль']")
    LOGIN_BUTTON1 = (By.XPATH, "//button[@id='loginBtn']")


class SecondStepScenarioLocators:
    RADIOBUTTON_GOAL = (By.XPATH, "//mat-radio-button")
    ZAPUSK_KOMPANII_BUTTON = (By.XPATH, '//p[@class="title"][text()="Запуск первой рекламной кампании"]')
    NEXT_BUTTON = (By.XPATH, "//button[@type='button']")
    NO_BUTTON = (By.XPATH, "//button[contains(text(),'Нет')]")
    SLIDER = (By.XPATH, "//mat-slider")
    CITY_FIELD = (By.XPATH, "//input[@placeholder='Введите город']")
    REGION_SUBMENU = (By.XPATH, "//span[@class='mat-option-text']")
    STEP_COUNTER = (By.CSS_SELECTOR, "div[class='progress-bar-container--status']")

    # login
    START_BUTTON = (By.XPATH, "//button[@id='start']")
    VHOD_BUTTON = (By.XPATH, "//a[@role='tab'][@aria-selected='false'][text()='Вход']")
    EMAIL_FIELD = (By.XPATH, "//form[@class='login ng-untouched ng-pristine ng-invalid']//input[@placeholder='Ваш e-mail']")
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password'][@placeholder='Пароль']")
    LOGIN_BUTTON1 = (By.XPATH, "//max-file-uploader")


class ThirdStepScenarioLocators:
    ZAPUSK_KOMPANII_BUTTON = (By.XPATH, '//p[@class="title"][text()="Запуск первой рекламной кампании"]')
    NEXT_BUTTON = (By.XPATH, "//button[@type='button']")
    USERS_COUNT = (By.XPATH, "//input[@placeholder='Количество посетителей']")
    UPLOAD_FILE = (By.XPATH, "//label[@for='1677597784849']")



    # login
    START_BUTTON = (By.XPATH, "//button[@id='start']")
    VHOD_BUTTON = (By.XPATH, "//a[@role='tab'][@aria-selected='false'][text()='Вход']")
    EMAIL_FIELD = (By.XPATH, "//form[@class='login ng-untouched ng-pristine ng-invalid']//input[@placeholder='Ваш e-mail']")
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password'][@placeholder='Пароль']")
    LOGIN_BUTTON1 = (By.XPATH, "//button[@id='loginBtn']")
