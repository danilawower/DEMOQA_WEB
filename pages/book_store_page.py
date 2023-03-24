from locators.book_store_page import LoginPageLocators
from pages.base_page import BasePage


class BookStoreLoginPage(BasePage):
    locators = LoginPageLocators()

    def commit_login(self):
        self.element_is_clickable(self.locators.LOGIN_FIELD).send_keys('username1')
        self.element_is_present(self.locators.PASSWORD_FIELD).send_keys('@#wTmBpo4')
        self.element_is_clickable(self.locators.LOGIN_BUTTON).click()

