import random

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generated_color, generated_date

from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num):
        accordian = {'first':  #обозначаем, что у первого тайтл и контент такой, у второго и третьего - иной
                         {'title':self.locators.SECTION_FIRST,
                          'content':self.locators.SECTION_FIRST_CONTENT},
                     'second':
                         {'title': self.locators.SECTION_SECOND,
                          'content': self.locators.SECTION_SECOND_CONTENT},
                     'third':
                         {'title': self.locators.SECTION_THIRD,
                          'content': self.locators.SECTION_THIRD_CONTENT},
                     }

        section_title = self.element_is_visible(accordian[accordian_num]['title']) #забираем по словарю тайтл
        try:
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        except TimeoutException:
            section_title.click()
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        return [section_title.text, len(section_content)]  #тут забираем текст тайтла, ибо мы на него только лишь кликали.


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    def fill_input_multi_autocomplete(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 4)) #sample выбирает рандом значение из списка. k=1 показывает сколько их надо нам
        for color in colors: #color как доп. переменная colors
            input_multi = self.element_is_clickable(self.locators.MULTI_INPUT)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER) #цикл перебирания, чтобы селениум понял, сколько раз жать Enter после рандомного кол-ва значений
        return colors

    def remove_value_from_multi(self):
        count_value_before = len(self.elements_are_present(self.locators.MULTI_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.MULTI_VALUE_REMOVE)
        for value in remove_button_list:    #value как переменная remove_button_list
            value.click()
            break  #прерывание, чтобы выходить из этого потока
        count_value_after = len(self.elements_are_present(self.locators.MULTI_VALUE))
        return count_value_before, count_value_after

    def check_color_in_multi(self):
        color_list = self.elements_are_present(self.locators.MULTI_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    def fill_input_single(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.element_is_clickable(self.locators.SINGLE_INPUT)
        input_single.send_keys(color)
        return color[0]

    def check_color_single(self):
        color = self.element_is_present(self.locators.SINGLE_CONTAINER)
        return color.text


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    def select_date(self):
        date = next(generated_date())
        date_input = self.element_is_visible(self.locators.DATE_INPUT)
        value_date_before = date_input.get_attribute('value') #берём атрибут значения, который был в поле дата
        date_input.click()
        self.select_date_by_text(self.locators.DATE_SELECT_MONTH, date.month) #используем функцию ниже и подставляем генерир. дату
        self.select_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.select_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = date_input.get_attribute('value')
        return value_date_after, value_date_before

    def select_date_by_text(self, element, value):
        select = Select(self.elements_are_present(element)) # Select выбирать элемент по какому то параметру. например по впидимому тексту
        select.select_by_visible_text(value)

    def select_date_item_from_list(self, elements, value):
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:  #если текстовое значение элемента(название месяца) совпадает с значением в списке(календаре) то кликаем го
                item.click()
                break



