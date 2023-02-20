import base64
import os
import random
import requests
from selenium.common import TimeoutException
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from generator.generator import generated_person, generated_file
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators, ButtonsPageLocators, LinksPageLocators, UploadAndDownloadPageLocators, \
    DynamicPropertiesPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
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
        count = 21  # всего их 21 штука
        while count != 0:  # когда число не равно нулю то делаем следующее:
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


# def get_output_result(self):
#    result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
#    data = []
#    for item in result_list:
#        data.append(item.text)
#   return data


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    def click_on_the_radio_button(self):  # choice делает выборку и прокликивает по всем батоном с определенынм локатром
        self.element_is_visible(self.locators.YES_RADIOBUTTON).click()
        self.element_is_visible(self.locators.NO_RADIOBUTTON).click()
        self.element_is_visible(self.locators.IMPRESSIVE_RADIOBUTTON).click()
        # choices = {'yes': self.locators.YES_RADIOBUTTON,
        # 'impressive': self.locators.IMPRESSIVE_RADIOBUTTON,
        # 'no': self.locators.NO_RADIOBUTTON}

        # self.element_is_visible(choices[choice]).click()

    def output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT)


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    def add_new_person(self, count=1):  # 1 Paз провести добавление персоны
        while count != 0:  # если количество не равно нулю, то делаем
            person_info = next(generated_person())  # берем из генератор и функции generated person
            firstname = person_info.firstname
            lastname = person_info.lastname
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(firstname)
            self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(lastname)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT).click()

            count -= 1
            return [firstname, lastname, str(age), email, str(salary),
                    department]  # вводим данные списком и строковыми значениями, чтобы они совпали с выведенными данными

    def check_new_added_person(self):
        person_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []  # данные списком
        for item in person_list:
            data.append(item.text.splitlines())  # добавить данные текстовые, разделяя линии
        return data

    def search_some_person(self, key_word):  # по ключевому слову
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    def check_search_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element(By.XPATH, ".//ancestor::span[@class='rt-tr-group']")
        return row.text.splitlines()  # возвращаем значение row его текст, разделяя линии

    def update_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT).click()
        return str(age)  # выведем(вернём) строоковое значение годов


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    def click_on_different_button(self, type_click):  # тип клика, можно задать разные типы
        if type_click == "double":
            self.action_double_click(self.element_is_visible(self.locators.DOUBLE_BUTTON))
            return self.check_clicked_on_the_button(
                self.locators.SUCCESS_DOUBLE)  # ретёрним результаты используя функцию ниже

        if type_click == "right":
            self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))
            return self.check_clicked_on_the_button(self.locators.SUCCESS_RIGHT)

        if type_click == "click":
            self.element_is_visible(self.locators.CLICK_ME_BUTTON).click()
            return self.check_clicked_on_the_button(self.locators.SUCCESS_CLICK_ME)

    def check_clicked_on_the_button(self, element):
        return self.element_is_present(element).text


class LinksPage(BasePage):
    locators = LinksPageLocators()

    def check_new_tab_simple_link(self):
        simple_link = self.elements_are_visible(self.locators.SIMPLE_LINK)
        link_href = simple_link.getattribute('href')
        request = requests.get(f"{link_href}")  # request функция запросов
        if request.status_code == 200:
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])  # переключает на окно с иднексом один(второе)
            url = self.driver.current_url
            return link_href, url
        else:
            return link_href, request.status_code

    def check_broken_link(self, url):
        request = requests.get(url)  # этот юрл мы указываем в тесте
        if request.status_code == 200:
            self.element_is_present(self.locators.BAD_REQUEST).click()
        else:
            return request.status_code


class UploadAndDownloadPage(BasePage):
    locators = UploadAndDownloadPageLocators()

    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_present(self.locators.UPLOAD_FILE).send_keys(
            path)  # отправляем кейсами сам путь файла, из generator.py
        os.remove(path)  # удаление операц. системой файла
        text = self.element_is_present(self.locators.UPLOADED_FILE).text


    def download_file(self):
        link = self.element_is_clickable(self.locators.DOWNLOAD_FILE).click()





class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesPageLocators()

    def check_enable_button(self):
        time.sleep(6)
        try:
            self.element_is_clickable(self.locators.ENABLE_BUTTON)
        except TimeoutException:  # добавляем таймаут в исключения
            return False
        return True

    def check_color_change(self):
        color_button = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON)
        color_button_before = color_button.value_of_css_property('color')  # метод берущий свойство CSS (например цвет)
        time.sleep(6)
        color_button_after = color_button.value_of_css_property('color')
        return color_button_after, color_button_before

    def check_appear_button(self):
        time.sleep(6)
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER_FIVE_SEC_BUTTON)
        except TimeoutException:
            return False
        return True
