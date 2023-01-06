import random

from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators
from pages.base_page import BasePage
import time


class TextBoxPage(BasePage):  # basepage указал какие параметры использовать для нахождения элемента с base_page
    locators = TextBoxPageLocators  # указали локаторы со страницы элемент пейдж локаторс

    def fill_all_fields(self):
        person_info = next(generated_person())  # подтягиваем из генератора и некстом берем по одному рандомному данному
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(
            full_name)  # элемент виден из бейз пейджа, локатор из элемент пейдж локатор. отправляем дату из генеретейд выше
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_present(
            self.locators.CREATED_FULL_NAME).text  # элемент присутствует. локаторы тоже из элемент пейдж локаторс text
        email = self.element_is_present(self.locators.CREATED_EMAIL).text
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text
        return full_name, email, current_address, permanent_address  # показать что вывело


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(
            self.locators.ITEM_LIST)  # создаём список видимых локаторов(много чекбоксов)
        #  for item in item_list: создаем список элементов в этом самом листе
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]  # делаем рандомную выборку элементов в списке
            if count > 0:
                self.go_to_element(item)
                item.click()
                print(item)
                count -= 1
            else:
                break


   # def get_checked_chekboxes(self):
    #    checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
    #    data = []
    #    for box in checked_list:
    #        title_item = box.find_element_by_xpath(self.locators.TITLE_ITEM)
    #        data.append(title_item.text)
    #    return data


    #def get_output_result(self):
    #    result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
    #    data = []
    #    for item in result_list:
     #        data.append(item.text)
     #   return data

