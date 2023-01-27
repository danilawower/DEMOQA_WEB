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


class FramesPageLocators:
    FIRST_FRAME = (By.XPATH, "//iframe[@id='frame1']")
    SECOND_FRAME = (By.XPATH, "//iframe[@id='frame2']")
    TITLE_NAME = (By.XPATH, "//h1[@id='sampleHeading']")


class NestedFramesPageLocators:
    CHILD_FRAME = (By.XPATH, "//iframe[@srcdoc='<p>Child Iframe</p>']")
    PARENT_FRAME = (By.XPATH, "//iframe[@id='frame1']")
    CHILD_FRAME_TEXT = (By.CSS_SELECTOR, "p")
    PARENT_FRAME_TEXT = (By.CSS_SELECTOR, "body")


class ModalWindowsPageLocators:
    SMALL_MODAL_BUTTON = (By.XPATH, "//button[@id='showSmallModal']")
    LARGE_MODAL_BUTTON = (By.XPATH, "//button[@id='showLargeModal']")
    SMALL_MODAL_CLOSE_BUTTON = (By.XPATH, "//button[@id='closeSmallModal']")
    LARGE_MODAL_CLOSE_BUTTON = (By.XPATH, "//button[@id='closeLargeModal']")
    SMALL_BUTTON_TITLE = (By.XPATH, "//div[@id='example-modal-sizes-title-sm']")
    LARGE_BUTTON_TITLE = (By.XPATH, "//div[@id='example-modal-sizes-title-lg']")
    SMALL_BUTTON_BODY = (By.XPATH, "//div[@class='modal-body']")
    LARGE_BUTTON_BODY = (By.XPATH, "//p[contains(text(),'Lorem Ipsum is simply dummy text of the printing a')]")
