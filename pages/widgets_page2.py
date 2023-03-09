import random
import time

from selenium.webdriver import Keys

from generator.generator import generated_color
from locators.widgets_page_locators2 import AccordianLocators, AutocompleteLocators, SliderPageLocators, \
    ProgressbarPageLocators, TabsPageLocators, ToolTipsLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianLocators()

    def check_accordian(self, num):
        accordian = {'first': self.locators.FIRST_SECTION, 'second': self.locators.SECOND_SECTION, 'third':
                     self.locators.THIRD_SECTION}
        self.element_is_clickable(accordian[num]).click()


class AutocompletePage(BasePage):
    locators = AutocompleteLocators()

    def check_multiple_color(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 4))
        input_multi = self.element_is_present(self.locators.MULTI_COLOR)
        for color in colors:
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)


    def delete_multi(self):
        delete_multi = self.elements_are_present(self.locators.REMOVE_BUTTON)
        for button in delete_multi:
            button.click()

    def check_single_color(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        input_color = self.element_is_present(self.locators.SINGLE_COLOR)
        input_color.send_keys(color)
        input_color.send_keys(Keys.ENTER)



class SliderPage(BasePage):
    locators = SliderPageLocators()

    def check_slider(self):
        slider = self.element_is_present(self.locators.SLIDER)
        value_before = self.element_is_present(self.locators.SLIDER).get_attribute('value')
        self.action_drag_and_drop_by_offset(slider, random.randint(1, 100), 0)
        value_after = self.element_is_present(self.locators.SLIDER).get_attribute('value')
        return value_before, value_after


class ProgressbarPage(BasePage):
    locators = ProgressbarPageLocators()

    def check_progressbar(self):
        before = self.element_is_present(self.locators.BAR).get_attribute('aria-valuenow')
        self.element_is_clickable(self.locators.BUTTON).click()
        time.sleep(random.randint(1, 5))
        self.element_is_clickable(self.locators.BUTTON).click()
        after = self.element_is_present(self.locators.BAR).get_attribute('aria-valuenow')
        return before, after


class TabsPage(BasePage):
    locators = TabsPageLocators()

    def check_tabs(self, number):
        tabs = {'what': self.locators.WHAT, 'origin': self.locators.ORIGIN, 'use': self.locators.USE}
        self.element_is_clickable(tabs[number]).click()


    def check_random_tab(self):
        tabs = {'what': self.locators.WHAT, 'origin': self.locators.ORIGIN, 'use': self.locators.USE}
        self.element_is_clickable(random.choice(list(tabs.values()))).click()



class ToolTipsPage(BasePage):
    locators = ToolTipsLocators()

    def check_tooltip(self):
        button = self.element_is_present(self.locators.HOVER_BUTTON)
        self.action_move_to_element(button)
        text = self.element_is_present(self.locators.TOOL_TIP_INNERS)
        return text.text










