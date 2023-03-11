from selenium.webdriver.common.by import By


class SortablePageLocators:
    LIST_TAB = (By.XPATH, "//a[@id='demo-tab-list']")
    LIST_ELEMENTS = (By.XPATH, "//div[@class='vertical-list-container mt-4']//div[@class = 'list-group-item list-group-item-action']")
    GRID_TAB = (By.XPATH, "//a[@id='demo-tab-grid']")
    GRID_ELEMENTS = (By.XPATH, "//div[@class='create-grid']//div[@class = 'list-group-item list-group-item-action']")


class SelectablePageLocators:
    LIST_ELEMENTS = (By.XPATH, "//li[@class = 'mt-2 list-group-item list-group-item-action']")
    LIST_TAB = (By.XPATH, "//a[@id='demo-tab-list']")
    GRID_TAB = (By.XPATH, "//a[@id='demo-tab-grid']")
    GIRD_ELEMENTS = (By.XPATH, "//li[@class='list-group-item list-group-item-action']")
    LIST_ELEMENTS_ACTIVE = (By.XPATH, "//li[@class = 'mt-2 list-group-item active list-group-item-action']")
    GRID_ELEMENTS_ACTIVE = (By.XPATH, "//li[@class='list-group-item active list-group-item-action']")


