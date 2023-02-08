from selenium.webdriver.common.by import By


class SortablePageLocators:
    TAB_LIST = (By.XPATH, "//a[@id='demo-tab-list']")
    GRID_LIST = (By.XPATH, "//a[@id='demo-tab-grid']")
    LIST_ITEM = (By.CSS_SELECTOR, "div[class='vertical-list-container mt-4'] div[class='list-group-item "
                                  "list-group-item-action']")
    GRID_ITEM = (By.CSS_SELECTOR, 'div[class="create-grid"] div[class="list-group-item list-group-item-action"]')


class SelectablePageLocators:
    TAB_LIST = (By.XPATH, "//a[@id='demo-tab-list']")
    GRID_LIST = (By.XPATH, "//a[@id='demo-tab-grid']")
    LIST_ITEM = (By.CSS_SELECTOR, 'li[class="mt-2 list-group-item list-group-item-action"]')
    LIST_ITEM_ACTIVE = (By.CSS_SELECTOR, 'li[class="mt-2 list-group-item active list-group-item-action"]')
    GRID_ITEM = (By.CSS_SELECTOR, 'li[class="list-group-item list-group-item-action"]')
    GRID_ITEM_ACTIVE = (By.CSS_SELECTOR, 'li[class="list-group-item active list-group-item-action"]')


class ResizablePageLocators:
    RESIZABLE = (By.XPATH, "//div[@class='text'][normalize-space()='Resizable']")
    RESIZABLE_BOX_HANDLE = (By.XPATH, "//div[@id='resizableBoxWithRestriction']//span[@class='react-resizable-handle "
                                      "react-resizable-handle-se']")
    RESIZABLE_BOX = (By.XPATH, "//div[@id='resizableBoxWithRestriction']")
    RESIZABLE_HANDLE = (By.XPATH, "//div[@id='resizable']//span[@class='react-resizable-handle "
                                  "react-resizable-handle-se']")


class DroppablePageLocators:

#simple
    SIMPLE_TAB = (By.XPATH, "//a[@id='droppableExample-tab-simple']")
    DRAG_ME_SIMPLE = (By.XPATH, "//div[@id='draggable']")
    DROP_HERE_SIMPLE = (By.XPATH, "//div[@id='simpleDropContainer']//div[@id='droppable']")

#accept
    ACCEPT_TAB = (By.XPATH, "//a[@id='droppableExample-tab-accept']")
    ACCEPTABLE = (By.XPATH, "//div[@id='acceptable']")
    NOT_ACCEPTABLE = (By.XPATH, "//div[@id='notAcceptable']")
    DROP_HERE_ACCEPT = (By.XPATH, "//div[@id='acceptDropContainer']//div[@id='droppable']")

#prevent
    PREVENT_TAB = (By.XPATH, "//a[@id='droppableExample-tab-preventPropogation']")
    DRAG_ME_PREVENT = (By.XPATH, "//div[@id='dragBox']")
    OUTER_DROPPABLE_NOT = (By.XPATH, "//div[@id='notGreedyDropBox']")
    INNER_DROPPABLE_NOT = (By.XPATH, "//div[@id='notGreedyInnerDropBox']")
    INNER_DROPPABLE_GREEDY = (By.XPATH, "//div[@id='greedyDropBoxInner']")
    OUTER_DROPPABLE_GREEDY = (By.XPATH, "//div[@id='greedyDropBox']")

#revert
    REVERT_TAB = (By.XPATH, "//a[@id='droppableExample-tab-revertable']")
    WILL_REVERT = (By.XPATH, "//div[@id='revertable']")
    NOT_REVERT = (By.XPATH, "//div[@id='notRevertable']")
    DROP_HERE_REVERT = (By.XPATH, "//div[@id='revertableDropContainer']//div[@id='droppable']")


class DraggablePageLocators:
    #simple
    DRAG_ME = (By.XPATH, "//div[@id='dragBox']")
    AXIS_TAB = (By.XPATH, "//a[@id='draggableExample-tab-axisRestriction']")
    ONLY_X = (By.XPATH, "//div[@id='restrictedX']")
    ONLY_Y = (By.XPATH, "//div[@id='restrictedY']")




