import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys



class BasePage:



    def __init__(self, driver, url):
        self.driver = driver
        self.url = url


    def open(self):  # открыть страницу в тесте будет page.open
        self.driver.get(self.url)


    def element_is_visible(self, locator, timeout=5): # ищу элемент по локатору пока он не будет показан(wait)
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5): # всех элементов найденных
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5): # всех элементов присутсвующих
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5): #невидимый элемент
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5): #кликабельный элемент
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))


    def go_to_element(self, element): #скроллим до элемента
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


    def action_double_click(self, element):
        action = ActionChains(self.driver) #вызываем функцию actionchains
        action.double_click(element) #дабл кликаем этой функцией на элемент
        action.perform() #подтвердить действие



    def action_drag_and_drop_by_offset(self, element, x_coords, y_coords): #тянем в стороны, указываем координаты х и у
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_coords, y_coords)  #зажимает кнопку мыши и двигает  в указанном направлении
        action.perform()



    def action_drag_and_drop_to_element(self, what, where): #тянет сортаблы и драг эн дроп элементы, вниз вверх и тд
        action = ActionChains(self.driver)
        action.drag_and_drop(what, where)
        action.perform()

    def action_open_new_tab(self, element):
        action = ActionChains(self.driver)
        action.key_down(Keys.CONTROL)
        action.click(element)
        action.key_up(Keys.CONTROL)
        action.perform()



    def action_move_to_element(self, element): #навести элемент
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()


    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element) #context-click = (right click) on an element.
        action.perform()




