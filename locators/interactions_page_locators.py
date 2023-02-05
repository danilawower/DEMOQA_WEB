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