import random
import time

import when as when

from generator.generator import generated_person
from locators.elements_page_locators2 import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):

    locators = TextBoxPageLocators()

    def check_textbox(self):
        person = next(generated_person())
        self.element_is_visible(self.locators.FULL_NAME_FIELD).send_keys(person.full_name)
        self.element_is_visible(self.locators.EMAIL_FIELD).send_keys(person.email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS_FIELD).send_keys(person.current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS_FIELD).send_keys(person.permanent_address)
        self.element_is_clickable(self.locators.SUBMIT_BUTTON).click()


class CheckBoxPage(BasePage):

    locators = CheckBoxPageLocators()

    def expand_all_function(self): #раскрываем все чекбоксы этой функцией
        item_button = self.elements_are_present(self.locators.CHECKBOX_OPEN_BUTTON)
        for item in item_button:
            self.element_is_clickable(item)
            item.click()
        time.sleep(2)


    def check_checkbox(self):
        self.expand_all_function()
        self.expand_all_function()
        self.expand_all_function()
        item_list = self.elements_are_present(self.locators.CHECKBOX_LIST)
        count = 17
        while count != 0:
            item = item_list[random.randint(5, 10)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break


class RadioButtonPage(BasePage):

    locators = RadioButtonPageLocators()

    def check_radiobutton(self, list_num):
        item_list = {'yes': self.locators.YES_BUTTON, 'impressive': self.locators.IMPRESSIVE_BUTTON}
        self.element_is_clickable(item_list[list_num]).click()







