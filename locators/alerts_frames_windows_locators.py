from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:

    NEW_TAB_BUTTON = (By.XPATH, "//button[@id='tabButton']")
    TITLE_TEXT = (By.XPATH, "//h1[@id='sampleHeading']")
    NEW_WINDOW_BUTTON = (By.XPATH, "//button[@id='windowButton']")
