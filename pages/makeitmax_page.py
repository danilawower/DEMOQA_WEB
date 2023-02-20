import random
import time

from locators.makeitmax_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    locators = MainPageLocators()

    def check_main_page_registration(self):
        self.element_is_clickable(self.locators.START_BUTTON).click()
        email = self.element_is_clickable(self.locators.EMAIL_FIELD)
        email.send_keys('danilawower6@gmail.com')
        self.element_is_clickable(self.locators.CHOICE_BUSINESS).click()
        random.sample(self.elements_are_visible(self.locators.BUSINESS_LIST), k=1)[0].click()
        password = self.element_is_visible(self.locators.PASSWORD_FIELD)
        password.send_keys('132546Dar')
        password_repeat = self.element_is_visible(self.locators.PASSWORD_REPEAT_FIELD)
        password_repeat.send_keys('132546Dar')
        self.element_is_clickable(self.locators.CHECKBOX).click()
        self.element_is_clickable(self.locators.ACCEPT_BUTTON).click()

        time.sleep(3)
