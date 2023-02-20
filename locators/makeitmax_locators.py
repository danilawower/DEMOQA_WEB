from selenium.webdriver.common.by import By


class MainPageLocators:
    START_BUTTON = (By.XPATH, "//button[@id='start']")
    EMAIL_FIELD = (By.XPATH, "//input[@formcontrolname='email'][@class='form-control ng-untouched ng-pristine ng-invalid']")
    CHOICE_BUSINESS = (By.XPATH, "//span[text()='Отрасль вашего бизнеса']")
    BUSINESS_LIST = (By.XPATH, "//mat-option[@class='mat-option mat-focus-indicator ng-star-inserted']")
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password'][@placeholder='Пароль']")
    PASSWORD_REPEAT_FIELD = (By.XPATH, "//input[@type='password'][@placeholder='Повторите пароль']")
    CHECKBOX = (By.XPATH, "//span[@class='mat-checkbox-inner-container mat-checkbox-inner-container-no-side-margin']")
    ACCEPT_BUTTON = (By.XPATH, "//form[@class='register ng-dirty ng-touched ng-valid']//button[@id='registerBtn']")