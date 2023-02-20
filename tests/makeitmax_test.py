from pages.makeitmax_page import MainPage


class TestMakeItMax:
    class TestMainPageRegistration:

        def test_main_page_registration(self, driver):
            main_page_registration = MainPage(driver, 'https://makeitmax.ru/')
            main_page_registration.open()
            main_page_registration.check_main_page_registration()
