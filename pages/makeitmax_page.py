import random
import time

from generator.generator import generated_person
from locators.makeitmax_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    locators = MainPageLocators()

    def check_main_page_registration(self):
        person = next(generated_person())
        self.element_is_clickable(self.locators.START_BUTTON).click()
        email = self.element_is_clickable(self.locators.EMAIL_FIELD)
        email.send_keys(person.email)
        self.element_is_clickable(self.locators.CHOICE_BUSINESS).click()
        business_list = self.elements_are_present(self.locators.BUSINESS_LIST)
        count = 15
        while count != 0:
            item = business_list[random.randint(1, 1)]
            if count > 0:
                self.go_to_element(item)
                item.click()
            break
        password = self.element_is_visible(self.locators.PASSWORD_FIELD)
        password.send_keys('132546Dar')
        password_repeat = self.element_is_visible(self.locators.PASSWORD_REPEAT_FIELD)
        password_repeat.send_keys('132546Dar')
        self.element_is_clickable(self.locators.CHECKBOX).click()
        self.element_is_clickable(self.locators.ACCEPT_BUTTON).click()

        time.sleep(3)
