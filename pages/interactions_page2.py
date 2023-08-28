import random
import time

from locators.interaction_page_locators2 import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppableLocators
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


class ResizablePage(BasePage):
    locators = ResizablePageLocators()

    def check_parameters(self):
        box = self.element_is_present(self.locators.RESIZABLE_BOX)
        values = box.get_attribute('style')
        return values

    def change_parameters(self):
        before = self.check_parameters()
        handle = self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE)
        self.action_drag_and_drop_by_offset(handle, random.randint(1, 200), random.randint(1, 200))
        after = self.check_parameters()
        return before, after



class DroppablePage(BasePage):
    locators = DroppableLocators()

    def check_droppable_simple(self):
        drag_element = self.element_is_present(self.locators.DRAG_ME)
        drop_element = self.element_is_present(self.locators.DROP_HERE)
        self.action_drag_and_drop_to_element(drag_element, drop_element)
        text = drop_element.text
        #return text




    def check_droppable_accept(self):
        self.element_is_clickable(self.locators.ACCEPT_BUTTON).click()
        acceptable = self.element_is_present(self.locators.ACCEPTABLE)
        drop_here = self.element_is_present(self.locators.DROP_HERE_ACCEPT)
        not_acceptable = self.element_is_present(self.locators.NOT_ACCEPTABLE)
        self.action_drag_and_drop_to_element(not_acceptable, drop_here)
        text_not_accept = drop_here.text
        self.action_drag_and_drop_to_element(acceptable, drop_here)
        text_accept = drop_here.text
        return text_not_accept, text_accept







