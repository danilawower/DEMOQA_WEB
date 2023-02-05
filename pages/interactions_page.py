import random

from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators()

    def get_sortable_items(self, elements):
        item_list = self.elements_are_visible(elements) #метод для получения элементов, в каком порядке они сейчас
        return [item.text for item in item_list] #возвращаем их текстовое значение


    def change_list_order(self):
        self.element_is_visible(self.locators.TAB_LIST).click() #кликаем на список, чтобы он был открыт наверняка
        order_before = self.get_sortable_items(self.locators.LIST_ITEM) #получаем методом прошлый порядок "до". elements - как раз локатор на элементы
        item_list = random.sample(self.elements_are_visible(self.locators.LIST_ITEM), k=2) #выбираем рандомные элементы. 2 штуки
        item_what = item_list[0] #какой айтем нужно двигать
        item_where = item_list[1] #на чьё место, куда айтем двигать
        self.action_drag_and_drop_to_element(item_what, item_where) #драг энд дропаем эти элементы и указываем куда
        order_after = self.get_sortable_items(self.locators.LIST_ITEM)
        return order_after, order_before


    def change_grid_order(self):
        self.element_is_visible(self.locators.GRID_LIST).click()
        order_before = self.get_sortable_items(self.locators.GRID_ITEM)
        item_list = random.sample(self.elements_are_visible(self.locators.GRID_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(self.locators.GRID_ITEM)
        return order_before, order_after


class SelectablePage(BasePage):
    locators = SelectablePageLocators()

    def click_selectable_item(self, elements):
        item_list = self.elements_are_visible(elements)
        random.sample(item_list, k=1)[0].click() #кликаем один раз


    def select_list_item(self):
        self.element_is_visible(self.locators.TAB_LIST).click()
        self.click_selectable_item(self.locators.LIST_ITEM)
        active_element = self.element_is_visible(self.locators.LIST_ITEM_ACTIVE)
        return active_element.text

    def select_grid_item(self):
        self.element_is_visible(self.locators.GRID_LIST).click()
        self.click_selectable_item(self.locators.GRID_ITEM)
        active_element = self.element_is_visible(self.locators.GRID_ITEM_ACTIVE)
        return active_element.text






