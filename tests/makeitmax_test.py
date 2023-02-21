from pages.makeitmax_page import MainPage, MainPageLogin, ProfilePage


class TestMakeItMax:
    class TestMainPageRegistration:

        def test_main_page_registration(self, driver):
            main_page_registration = MainPage(driver, 'https://makeitmax.ru/')
            main_page_registration.open()
            main_page_registration.check_main_page_registration()


    class TestLoginLogout:

        def test_login_logout(self, driver):
            login_logout_page = MainPageLogin(driver, 'https://makeitmax.ru/')
            login_logout_page.open()
            login_logout_page.check_login_logout()


    class TestProfileChange:

        def test_profile_change(self, driver):
            profile_page = ProfilePage(driver, 'https://makeitmax.ru/')
            profile_page.open()
            profile_page.check_change_profile()
