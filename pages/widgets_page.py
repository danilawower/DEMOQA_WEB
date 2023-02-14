import random
import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generated_color, generated_date

from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators, \
    SliderProgressBarPage, TabsPageLocators, ToolTipsLocators, MenuPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num): #создаем словарь
        accordian = {'first':  # обозначаем, что у первого тайтл и контент такой, у второго и третьего - иной
                         {'title': self.locators.SECTION_FIRST,
                          'content': self.locators.SECTION_FIRST_CONTENT},
                     'second':
                         {'title': self.locators.SECTION_SECOND,
                          'content': self.locators.SECTION_SECOND_CONTENT},
                     'third':
                         {'title': self.locators.SECTION_THIRD,
                          'content': self.locators.SECTION_THIRD_CONTENT},
                     }

        section_title = self.element_is_visible(
            accordian[accordian_num]['title'])  # выбираем по словарю тайтл и укахываем что делаем(ниже клик)
        try:
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        except TimeoutException:
            section_title.click()
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        return [section_title.text,
                len(section_content)]  # тут забираем текст тайтла, ибо мы на него только лишь кликали.


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    def fill_input_multi_autocomplete(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2,
                                                                                    4))  # sample выбирает рандом значение из списка. k=1 показывает сколько их надо нам
        for color in colors:  # color как доп. переменная colors
            input_multi = self.element_is_clickable(self.locators.MULTI_INPUT)
            input_multi.send_keys(color)
            input_multi.send_keys(
                Keys.ENTER)  # цикл перебирания, чтобы селениум понял, сколько раз жать Enter после рандомного кол-ва значений
        return colors

    def remove_value_from_multi(self):
        count_value_before = len(self.elements_are_present(self.locators.MULTI_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.MULTI_VALUE_REMOVE)
        for value in remove_button_list:  # value как переменная remove_button_list
            value.click()
            break  # прерывание, чтобы выходить из этого потока
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
        value_date_before = date_input.get_attribute('value')  # берём атрибут значения, который был в поле дата
        date_input.click()
        self.select_date_by_text(self.locators.DATE_SELECT_MONTH,
                                 date.month)  # используем функцию ниже и подставляем генерир. дату
        self.select_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.select_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = date_input.get_attribute('value')
        return value_date_after, value_date_before

    def select_date_by_text(self, element, value):
        select = Select(self.elements_are_present(
            element))  # Select выбирать элемент по какому то параметру. например по впидимому тексту
        select.select_by_visible_text(value)

    def select_date_item_from_list(self, elements, value):
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:  # если текстовое значение элемента(название месяца) совпадает с значением в списке(календаре) то кликаем го
                item.click()
                break


class SliderProgressBarPage(BasePage):
    locators = SliderProgressBarPage()

    def change_slider_value(self):
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        slider_input = self.element_is_visible(self.locators.INPUT_SLIDER)
        self.action_drag_and_drop_by_offset(slider_input, random.randint(1, 100), 0)  # смотри base_page
        value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        return value_before, value_after

    def change_progress_bar(self):
        value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        progressbar_button = self.element_is_clickable(self.locators.PROGRESS_BAR_BUTTON)
        progressbar_button.click()
        time.sleep(random.randint(2, 5))
        progressbar_button.click()
        value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        return value_before, value_after


class TabsPage(BasePage):
    locators = TabsPageLocators()


    def check_tabs_list(self, list_tab_num):
        list_tab = {'what':
                        {'title': self.locators.TABS_WHAT,
                         'content': self.locators.TABS_WHAT_CONTENT},
                    'origin':
                        {'title': self.locators.TABS_ORIGIN,
                         'content': self.locators.TABS_ORIGIN_CONTENT},
                    'use':
                        {'title': self.locators.TABS_USE,
                         'content': self.locators.TABS_USE_CONTENT},
                    }
        button = self.element_is_clickable(list_tab[list_tab_num]['title'])
        button.click()
        content = self.element_is_visible(list_tab[list_tab_num]['content']).text
        return [button.text, len(content)]



class ToolTipsPage(BasePage):
    locators = ToolTipsLocators()

    def get_text_from_tool(self, one, two): #наводим на элементт и ждем появления тултипа
        element = self.element_is_present(one) #элемент находим
        self.action_move_to_element(element) #на элемент наводим
        self.element_is_visible(two) #он становится видимым
        tool_tips_text = self.element_is_visible(self.locators.TOOL_TIP_INNERS) #у этого видимого элемента мы забираем текст
        text = tool_tips_text.text
        return text

    def check_tool_tips(self): #здесь вызываем прошлый метод, по этому порядок (one,two) был описан
        tool_tip_text_button = self.get_text_from_tool(self.locators.BUTTON, self.locators.BUTTON_HOVER_TEXT)
        tool_tip_text_field = self.get_text_from_tool(self.locators.FIELD, self.locators.FIELD_HOVER_TEXT)
        tool_tip_text_contrary = self.get_text_from_tool(self.locators.CONTRARY_LINK, self.locators.CONTRARY_HOVER_TEXT)
        tool_tip_text_section = self.get_text_from_tool(self.locators.SECTION_LINK, self.locators.SECTION_HOVER_TEXT)
        return tool_tip_text_button, tool_tip_text_field, tool_tip_text_contrary, tool_tip_text_section



class MenuPage(BasePage):
    locators = MenuPageLocators()

    def check_menu(self):
        menu_item_list = self.elements_are_present(self.locators.MENU_ITEM_LIST) #указываем на все пункты меню, что есть
        data = []
        for item in menu_item_list: #проходимся по ним циклом
            self.action_move_to_element(item) #action методом наводимся на каждый
            data.append(item.text) #подставляем к каждому итему .text чтобы забрать его текст
        return data #возвращаем текст списком

    def check_menu2(self):
        item = self.element_is_present(self.locators.MENU2)
        self.action_move_to_element(item)












