from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage
import time




class TextBoxPage(BasePage):  # basepage указал какие параметры использовать для нахождения элемента с base_page
    locators = TextBoxPageLocators  # указали локаторы со страницы элемент пейдж локаторс

    def fill_all_fields(self):
        person_info = next(generated_person())   #подтягиваем из генератора и некстом берем по одному рандомному данному
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)  #элемент виден из бейз пейджа, локатор из элемент пейдж локатор. отправляем дату из генеретейд выше
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address


    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text  #элемент присутствует. локаторы тоже из элемент пейдж локаторс text
        email = self.element_is_present(self.locators.CREATED_EMAIL).text
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text
        return full_name, email, current_address, permanent_address  #показать что вывело