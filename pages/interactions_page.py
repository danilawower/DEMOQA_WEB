import random
import time

from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators
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



class ResizablePage(BasePage):
    locators = ResizablePageLocators

    def get_px_from_width_height(self, value_of_size): #берем значения высоты и ширины(у первого и второго)
        width = value_of_size
        height = value_of_size
        return width, height


    def get_max_min_size(self, element):
        size = self.element_is_visible(element)
        size_value = size.get_attribute("style") #значение размеров в атрибуте 'style' см. devtools
        return size_value

    def change_size_resizable_box(self):
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), 200, 100)
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), -300, -100)
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        return min_size, max_size

    def change_size_resizable(self):
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_HANDLE),
                                            random.randint(1, 300), random.randint(1, 300))
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_HANDLE), -300, -100)
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        return min_size, max_size


class DroppablePage(BasePage):
    locators = DroppablePageLocators()

    def drop_simple(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME_SIMPLE)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_SIMPLE)
        self.action_drag_and_drop_to_element(drag_div, drop_div) #тянем элемент "из" "в"
        return drop_div.text


    def drop_accept(self):
        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        acceptable_div = self.element_is_visible(self.locators.ACCEPTABLE)
        not_acceptable_div = self.element_is_visible(self.locators.NOT_ACCEPTABLE)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_ACCEPT)
        self.action_drag_and_drop_to_element(not_acceptable_div, drop_div)
        drop_text_not_accept = drop_div.text
        self.action_drag_and_drop_to_element(acceptable_div, drop_div)
        drop_text_accept = drop_div.text
        return drop_text_not_accept, drop_text_accept

    def drop_prevent(self):
        self.element_is_visible(self.locators.PREVENT_TAB).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME_PREVENT)
        not_greedy_inner_box = self.element_is_visible(self.locators.INNER_DROPPABLE_NOT)
        greedy_inner_box = self.element_is_visible(self.locators.INNER_DROPPABLE_GREEDY)
        self.action_drag_and_drop_to_element(drag_div, not_greedy_inner_box)
        text_not_greedy_box = self.element_is_visible(self.locators.OUTER_DROPPABLE_NOT).text
        text_not_greedy_inner_box = not_greedy_inner_box.text
        self.action_drag_and_drop_to_element(drag_div, greedy_inner_box)
        text_greedy_box = self.element_is_visible(self.locators.OUTER_DROPPABLE_GREEDY).text
        text_greedy_inner_box = greedy_inner_box.text
        return text_not_greedy_box, text_not_greedy_inner_box, text_greedy_box, text_greedy_inner_box

    def drop_revert(self, type_drag):
        self.element_is_visible(self.locators.REVERT_TAB).click()
        drags = {'will': {'revert': self.locators.WILL_REVERT},
                 'not_will': {'revert': self.locators.NOT_REVERT}}
        revert = self.element_is_visible(drags[type_drag]['revert'])
        drop_div = self.element_is_visible(self.locators.DROP_HERE_REVERT)
        self.action_drag_and_drop_to_element(revert, drop_div)
        position_after_move = revert.get_attribute('style')
        time.sleep(1)
        position_after_revert = revert.get_attribute('style')
        return position_after_move, position_after_revert


