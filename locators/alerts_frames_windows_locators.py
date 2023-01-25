from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:

    NEW_TAB_BUTTON = (By.XPATH, "//button[@id='tabButton']")
    TITLE_TEXT = (By.XPATH, "//h1[@id='sampleHeading']")
    NEW_WINDOW_BUTTON = (By.XPATH, "//button[@id='windowButton']")
    NEW_TAB_TEXT = (By.XPATH, "//body[@xpath='1']")
    NEW_WINDOW_MESSAGE_BUTTON = (By.XPATH, "//button[@id='messageWindowButton']")


class AlertPageLocators:

    SEE_ALERT_BUTTON = (By.XPATH, "//button[@id='alertButton']")
    APPEAR_ALERT_5_SEC_BUTTON = (By.XPATH, "//button[@id='timerAlertButton']")
    CONFIRM_BOX_ALERT_BUTTON = (By.XPATH, "//button[@id='confirmButton']")
    PROMT_ALERT_BUTTON = (By.XPATH, "//button[@id='promtButton']")
    CONFIRM_RESULT = (By.XPATH, "//span[@id='confirmResult']")
    PROMT_RESULT = (By.XPATH, "//span[@id='promptResult']")
