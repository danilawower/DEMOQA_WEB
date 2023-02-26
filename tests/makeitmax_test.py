import time

from pages.makeitmax_page import MainPage, MainPageLogin, ProfilePage, FirsStepScenario, SecondStepScenario, \
    ThirdStepScenario


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


    class TestFirstStepScenario:

        def test_first_scenario(self, driver):
            first_scenario = FirsStepScenario(driver, "https://makeitmax.ru/")
            first_scenario.open()
            step_result = first_scenario.check_first_scenario()
            assert 'Шаг 2 из 7' in step_result


    class TestSecondStepScenario:

        def test_second_scenario(self, driver):
            second_scenario = SecondStepScenario(driver, "https://makeitmax.ru/")
            second_scenario.open()
            step_result = second_scenario.check_second_scenario()
            assert 'Шаг 4 из 7' in step_result


    class TestThirdStepScenario:

        def test_third_step_scenario(self, driver):
            third_scenario = ThirdStepScenario(driver, "https://makeitmax.ru/")
            third_scenario.open()
            third_scenario.check_third_scenario()






