from selenium.webdriver.common.by import By


class BrowserWindowsLocators:
    NEW_TAB = (By.XPATH, "//button[@id='tabButton']")
    NEW_WINDOW = (By.XPATH, "//button[@id='windowButton']")
    NEW_WINDOW_MESSAGE = (By.XPATH, "//button[@id='messageWindowButton']")
    TEXT = (By.XPATH, "//body[@xpath='1']")


class AlertsLocators:
    ALERT_BUTTON = (By.XPATH, "//button[@id='alertButton']")
    CONFIRM_BOX = (By.XPATH, "//button[@id='confirmButton']")
    ALERT_TEXT = (By.XPATH, "//button[@id='promtButton']")


class FramesLocators:
    FRAME1 = (By.XPATH, "//iframe[@id='frame1']")
    FRAME2 = (By.XPATH, "//iframe[@id='frame2']")


class NestedFramesLocators:
    CHILD_FRAME = (By.XPATH, "//iframe[@srcdoc='<p>Child Iframe</p>']")
    PARENT_FRAME = (By.XPATH, "//iframe[@id='frame1']")



class ModalDialogsLocators:
    SMALL_MODAL = (By.XPATH, "//button[@id='showSmallModal']")
    LARGE_MODAL = (By.XPATH, "//button[@id='showLargeModal']")
    CLOSE_SMALL = (By.XPATH, "//button[@id='closeSmallModal']")
    CLOSE_LARGE = (By.XPATH, "//button[@id='closeLargeModal']")





