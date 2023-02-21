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

    START_BUTTON = (By.XPATH, "//button[@id='start']")
    VHOD_BUTTON = (By.XPATH, "//a[@role='tab'][@aria-selected='false'][text()='Вход']")
    EMAIL_FIELD = (By.XPATH, "//form[@class='login ng-untouched ng-pristine ng-invalid']//input[@placeholder='Ваш e-mail']")
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password'][@placeholder='Пароль']")
    LOGIN_BUTTON1 = (By.XPATH, "//button[@id='loginBtn']")