import time

from locators.alerts_frames_windows_locators2 import BrowserWindowsLocators, AlertsLocators, FramesLocators, \
    NestedFramesLocators, ModalDialogsLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsLocators()

    def check_new_window(self):
        self.element_is_clickable(self.locators.NEW_WINDOW).click()
        self.driver.switch_to.window(self.driver.window_handles[1])

    def check_new_window_message(self):
        self.element_is_clickable(self.locators.NEW_WINDOW_MESSAGE).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text = self.element_is_visible(self.locators.TEXT).get_attribute('innerHTML').splitlines()[0]
        self.driver.switch_to.window(self.driver.window_handles[0])


class AlertPage(BasePage):  # alert = self.driver.switch_to.alert     alert.accept()    alert.send_keys
    locators = AlertsLocators()

    def check_alert_button(self):
        self.element_is_clickable(self.locators.CONFIRM_BOX).click()
        alert = self.driver.switch_to.alert
        alert.accept()

    def check_alert_text(self):
        self.element_is_clickable(self.locators.ALERT_TEXT).click()
        alert = self.driver.switch_to.alert
        alert.send_keys('Test')
        alert.accept()


class FramePage(BasePage):  # self.driver.switch_to.default_content()
    locators = FramesLocators()

    def check_frames(self, frame):
        if frame == 'frame1':
            frame = self.element_is_present(self.locators.FRAME1)
            height = frame.get_attribute('height')
            width = frame.get_attribute('width')
            self.driver.switch_to.frame(frame)
            self.driver.switch_to.default_content()
            return height, width
        if frame == 'frame2':
            frame2 = self.element_is_present(self.locators.FRAME2)
            height = frame2.get_attribute('height')
            width = frame2.get_attribute('width')
            self.driver.switch_to.frame(frame2)
            return height, width


class NestedFramePage(BasePage):
    locators = NestedFramesLocators()

    def check_nested_frames(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)


class ModalDialogsPage(BasePage):
    locators = ModalDialogsLocators()

    def check_modal_window(self):
        self.element_is_clickable(self.locators.SMALL_MODAL).click()
        self.element_is_clickable(self.locators.CLOSE_SMALL).click()
        self.element_is_clickable(self.locators.LARGE_MODAL).click()
        self.element_is_clickable(self.locators.CLOSE_LARGE).click()


