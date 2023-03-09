import time

from pages.alerts_frames_windows_page2 import BrowserWindowsPage, AlertPage, FramePage, NestedFramePage, \
    ModalDialogsPage


class TestAlertsFramesWindows:

    class TestBrowserWindows:
        def test_browser_window(self, driver):
            browser_window_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_window_page.open()
            browser_window_page.check_new_window_message()


    class TestAlert:
        def test_alert(self, driver):
            alert_page = AlertPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_page.check_alert_button()
            alert_page.check_alert_text()
            time.sleep(3)


    class TestFrames:
        def test_frames(self, driver):
            frames_page = FramePage(driver, "https://demoqa.com/frames")
            frames_page.open()
            frames_page.check_frames('frame1')
            frames_page.check_frames('frame2')


    class TestNestedFrames:
        def test_nested(self, driver):
            frames_page = NestedFramePage(driver, "https://demoqa.com/nestedframes")
            frames_page.open()
            frames_page.check_nested_frames()


    class TestModalDialogs:
        def test_modal(self, driver):
            modal_page = ModalDialogsPage(driver, "https://demoqa.com/modal-dialogs")
            modal_page.open()
            modal_page.check_modal_window()




