import random
import time
import requests

import when as when

from generator.generator import generated_person
from locators.elements_page_locators2 import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators, ButtonPageLocators, LinksPageLocators, UploadDownloadPageLocators, \
    DynamicPropertiesPageLocators
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




class RadioButtonPage(BasePage):  #self.element_is_clickable(item_list[list_num]).click()

    locators = RadioButtonPageLocators()

    def check_radiobutton(self, list_num):
        item_list = {'yes': self.locators.YES_BUTTON, 'impressive': self.locators.IMPRESSIVE_BUTTON}
        self.element_is_clickable(item_list[list_num]).click()





class WebTablePage(BasePage):

    locators = WebTablePageLocators()

    def add_new_person(self):
        person = next(generated_person())
        self.element_is_clickable(self.locators.ADD_BUTTON).click()
        self.element_is_present(self.locators.FIRST_NAME).send_keys(person.firstname)
        text = self.element_is_present(self.locators.FIRST_NAME).get_attribute('value')
        self.element_is_present(self.locators.LAST_NAME).send_keys(person.lastname)
        self.element_is_present(self.locators.EMAIL).send_keys(person.email)
        self.element_is_present(self.locators.AGE).send_keys(person.age)
        self.element_is_present(self.locators.SALARY).send_keys(person.salary)
        self.element_is_present(self.locators.DEPARTMENT).send_keys(person.department)
        self.element_is_clickable(self.locators.SUBMIT_BUTTON).click()
        return text

    def check_new_person(self):
        add_new = self.add_new_person()
        name = str(add_new)
        search = self.element_is_visible(self.locators.INPUT_SEARCH)
        search.send_keys(name)
        search_result = self.element_is_present(self.locators.TABLE_NAME).text
        return add_new, search_result



class ButtonsPage(BasePage):   # , (self, type_click):, if type_click == 'double':
    locators = ButtonPageLocators()

    def check_buttons(self, type_click):
        if type_click == 'double':
            double = self.element_is_clickable(self.locators.DOUBLE_CLICK)
            self.action_double_click(double)
        if type_click == 'right':
            right = self.element_is_clickable(self.locators.RIGHT_CLICK)
            self.action_right_click(right)
        if type_click == 'click':
            self.element_is_clickable(self.locators.CLICK_ME).click()



class LinksPage(BasePage):   #self.driver.switch_to.window(self.driver.window_handles[1])  # name = requests.get(url), return request.status_code
    locators = LinksPageLocators()

    def click_home_link(self):
        self.element_is_clickable(self.locators.HOME_LINK).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        url = self.driver.current_url
        return url



    def click_dynamic_link(self):
        self.element_is_clickable(self.locators.DYNAMIC_LINK).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        url = self.driver.current_url
        return url

    def click_forbidden_link(self):
        url = 'https://demoqa.com/forbidden'
        request = requests.get(url)
        return request.status_code




class UploadDownloadPage(BasePage):
    locators = UploadDownloadPageLocators()

    def check_download(self):
        self.element_is_clickable(self.locators.DOWNLOAD_BUTTON).click()
        #options = self.driver.ChromeOptions()
        #prefs = {"download.default_directory": "C:\\Users\daniil\\PycharmProjects\\automation_qa_course\\downloads"}
        #options.add_experimental_option("prefs", prefs)


    def check_upload(self):
        button = self.element_is_clickable(self.locators.UPLOAD_BUTTON)
        path = 'C:\\Users\\daniil\\Desktop\\python\\Screenshot_1.jpg'
        button.send_keys(path)



class DynamicPropertiesPage(BasePage):  #button.value_of_css_property('color')
    locators = DynamicPropertiesPageLocators()

    def check_enable_after_button(self):
        time.sleep(5)
        self.element_is_clickable(self.locators.ENABLE_AFTER_BUTTON).click()

    def check_color_change(self):
        button = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON)
        color_before = button.value_of_css_property('color')
        time.sleep(5)
        color_after = button.value_of_css_property('color')
        return color_before, color_after








