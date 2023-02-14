from selenium.webdriver.common.by import By


class RegistrationLocators:
    REGISTRATION = (By.XPATH, "//div[@class='b-header-top-container']//a[contains(text(),'Регистрация')]")
    PHYS_LICO = (By.XPATH, "//input[@type='radio'][@value='1']")
    CONTINUE = (By.XPATH, "//input[@value='Продолжить']")
    EMAIL_FIELD = (By.XPATH, "//input[@id='customer_email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='customer_password']")
    PASSWORD_CONFIRMATION = (By.XPATH, "//input[@id='customer_password_confirmation']")
    SURNAME_FIELD = (By.XPATH, "//input[@id='customer_family_name']")
    NAME_FIELD = (By.XPATH, "//input[@id='customer_name']")
    SURNAME2_FIELD = (By.XPATH, "//input[@id='customer_second_name']")
    PHONE_NUMBER = (By.XPATH, "//input[@id='customer_contact_attributes_phone']")
    RULE1 = (By.XPATH, "//input[@id='customer_term_of_service']")
    RULE2 = (By.XPATH, "//input[@id='customer_consent_of_processing_personal_data']")
    INDEX_FIELD = (By.XPATH, "//input[@id='customer_delivery_address_attributes_zip_code']")
    COUNTRY_FIELD = (By.XPATH, "//input[@id='customer_delivery_address_attributes_country']")
    REGISTRATION_CONFIRM = (By.XPATH, "//input[@value='Зарегистрироваться']")
    RESULT_TABLE = (By.XPATH, "//input[@autocomplete='off'][contains(@id,'customer_')]")
    LOGOUT_BUTTON = (By.XPATH, "//div[@class='b-header-top-container']//a[contains(text(),'Выход')]")


class PersonalAccountLocators:
    LOGIN_BUTTON = (
        By.XPATH, "//div[@class='b-header-top-container']//a[@class='b-link-user'][contains(text(),'Вход')]")
    LOGIN_EMAIL_FIELD = (By.XPATH, "//input[@id='customer_session_email']")
    LOGIN_PASSWORD_FIELD = (By.XPATH, "//input[@id='customer_session_password']")
    LOGIN_ENTER = (By.XPATH, "//input[@class='btn-reg']")
    LOGOUT_BUTTON = (By.XPATH, "//div[@class='b-header-top-container']//a[contains(text(),'Выход')]")


class ChangePersonalInformationLocators:
    CHANGE_INFO_BUTTON = (By.XPATH, "//a[contains(text(),'Редактировать профиль')]")
    LOGIN_BUTTON = (
        By.XPATH, "//div[@class='b-header-top-container']//a[@class='b-link-user'][contains(text(),'Вход')]")
    LOGIN_EMAIL_FIELD = (By.XPATH, "//input[@id='customer_session_email']")
    LOGIN_PASSWORD_FIELD = (By.XPATH, "//input[@id='customer_session_password']")
    LOGIN_ENTER = (By.XPATH, "//input[@class='btn-reg']")
    LOGOUT_BUTTON = (By.XPATH, "//div[@class='b-header-top-container']//a[contains(text(),'Выход')]")
    MY_ACCOUNT_BUTTON = (By.XPATH, "//div[@class='b-header-top-container']//a[@class='b-link-user'][contains(text(),"
                                   "'Мой кабинет')]")
    SAVE_BUTTON = (By.XPATH, "//input[@value='Сохранить']")
    SURNAME_FIELD = (By.XPATH, "//input[@id='customer_family_name']")


class ProductCatalogLocators:
    PRODUCT_CATALOG = (By.XPATH, "//button[@class='b-hbc-catalog-toggler']")
    MASLA = (By.XPATH, "//a[contains(text(),'Масла')]")
    MOTORNIE_MASLA = (By.XPATH, "//a[text()='Моторные масла']")
    PROIZVODITEL_LIST = (By.XPATH, "//div[@class='b-item-stm']")
    BUTTON_SHOW = (By.XPATH, "//button[@class = 'b-f2-btn-filter-show']")
    CHOISEN_PRODUCT = (By.XPATH, "//div[@class='b-f2-cc-right']//div[@class='b-item']")


class MenuHoverOverPageLocators:
    CLIENTAM = (By.XPATH, "//ul[@class='b-hbc-nav-list']//li[@class='dropdown']//a[@href='#'][contains(text(),"
                          "'Клиентам')]")
    BLOG = (By.XPATH, "//ul[@class='dropdown-menu show']//a[contains(text(),'Блог')]")
    MARSHAL_TV = (By.XPATH, "//ul[@class='dropdown-menu show']//a[contains(text(),'Маршал ТВ')]")
    NOVOSTI = (By.XPATH, "//ul[@class='dropdown-menu show']//a[contains(text(),'Новости')]")
    O_KOMPANII = (By.XPATH, "//ul[@class='dropdown-menu show']//a[contains(text(),'О компании')]")
    KONTAKTY = (By.XPATH, "//ul[@class='dropdown-menu show']//a[contains(text(),'Контакты')]")
    SUB_MENU = (By.XPATH, "//ul[@class='dropdown-menu show']")
    H1 = (By.XPATH, "//h1[@class='main-title']")


class CornerMenuLocators:
    MAIN_BUTTON = (By.CSS_SELECTOR, "a[class='b-link-toggler']")
    ELEMENTS = (By.XPATH, "//div[@class='b-ptsip-popup collapse b-ptsip-popup-without-dialog']//a[contains(@class, 'b-link')]")
    LOGIN_BUTTON = (
        By.XPATH, "//div[@class='b-header-top-container']//a[@class='b-link-user'][contains(text(),'Вход')]")
    LOGIN_EMAIL_FIELD = (By.XPATH, "//input[@id='customer_session_email']")
    LOGIN_PASSWORD_FIELD = (By.XPATH, "//input[@id='customer_session_password']")
    LOGIN_ENTER = (By.XPATH, "//input[@class='btn-reg']")
    ELEMENTS2 = (By.XPATH, "//span[@class='b-link-head']")
