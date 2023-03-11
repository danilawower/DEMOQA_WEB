import random

from locators.interaction_page_locators2 import SortablePageLocators, SelectablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators()

    def check_sortable_list(self):
        self.element_is_clickable(self.locators.LIST_TAB).click()
        list_elements = self.elements_are_present(self.locators.LIST_ELEMENTS)
        count = 6
        while count != 0:
            item = list_elements[random.randint(1, 6)]
            if count > 0:
                self.action_drag_and_drop_by_offset(item, random.randint(1, 5), 0)
                count -= 1
            else:
                break


    def check_sortable_grid(self):
        self.element_is_clickable(self.locators.GRID_TAB).click()
        grid_elements = self.elements_are_present(self.locators.GRID_ELEMENTS)
        count = 9
        while count != 0:
            item = grid_elements[random.randint(1, 9)]
            if count > 0:
                self.action_drag_and_drop_by_offset(item, random.randint(1, 5), random.randint(1, 5))
                count -= 1
            else:
                break


class SelectablePage(BasePage):
    locators = SelectablePageLocators()

    def check_selectable_list(self):
        self.element_is_clickable(self.locators.LIST_TAB).click()
        list_elements = self.elements_are_present(self.locators.LIST_ELEMENTS)
        for item in list_elements:
            item.click()
        list_elements_active = self.element_is_visible(self.locators.LIST_ELEMENTS_ACTIVE)
        return list_elements_active.text


    def check_selectable_grid(self):
        self.element_is_clickable(self.locators.GRID_TAB).click()
        list_elements = self.elements_are_present(self.locators.GIRD_ELEMENTS)
        for item in list_elements:
            item.click()
        list_elements_active = self.element_is_visible(self.locators.GRID_ELEMENTS_ACTIVE)
        return list_elements_active.text

