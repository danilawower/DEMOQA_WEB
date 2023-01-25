import random
import time

from locators.alerts_frames_windows_locators import BrowserWindowsPageLocators, AlertPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):

    locators = BrowserWindowsPageLocators

    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1]) #переключаемся на окно второе(по индексу 1)
        text_title = self.element_is_present(self.locators.TITLE_TEXT).text
        return text_title

    def check_opened_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TITLE_TEXT).text
        return text_title


class AlertPage(BasePage):

    locators = AlertPageLocators

    def check_see_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert #переключение на алерт
        return alert_window.text

    def check_alert_appear_5_sec(self):
        self.element_is_visible(self.locators.APPEAR_ALERT_5_SEC_BUTTON).click()
        time.sleep(6)
        alert_window = self.driver.switch_to.alert #переключение на алерт
        return alert_window.text

    def check_confirm_alert(self):
        self.element_is_visible(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept() #нажать на ОК в алерте
        text_result = self.element_is_present(self.locators.CONFIRM_RESULT).text
        return text_result

    def check_alert_prompt(self):
        text = f'Test{random.randint(0,100)}'
        self.element_is_visible(self.locators.PROMT_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text) #отправить текст внутрь алерта
        alert_window.accept()
        text_result = self.element_is_present(self.locators.PROMT_RESULT).text
        return text, text_result