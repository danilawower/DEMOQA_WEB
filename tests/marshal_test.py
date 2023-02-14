import time

from pages.marshal_page import PersonalAccountPage, RegistrationPage, ChangePersonalInformationPage, \
    ProductCatalogPage, MenuHoverOverPage, CornerMenuPage


class TestLogin:

    def test_login(self, driver):
        registration_page = RegistrationPage(driver, 'https://marshal.ru/')
        registration_page.open()
        button = registration_page.check_registration()
        assert button == 'Выход'


class TestPersonalAccount:

    def test_personal_account(self, driver):
        account_page = PersonalAccountPage(driver, "https://marshal.ru/")
        account_page.open()
        result = account_page.check_login()
        assert result == 'Выход'


class TestChangePersonalInformation:

    def test_change_personal(self, driver):
        change_info = ChangePersonalInformationPage(driver, "https://marshal.ru/")
        change_info.open()
        old, changed = change_info.check_change_personal_info()
        assert old != changed


class TestProductCatalog:

    def test_product_catalog(self, driver):
        product_catalog = ProductCatalogPage(driver, 'https://marshal.ru/')
        product_catalog.open()
        product_catalog.check_product_catalog()
        time.sleep(5)


class TestMenuHoverOver:

    def test_hover_over(self, driver):
        menu_over_hover = MenuHoverOverPage(driver, 'https://marshal.ru/')
        menu_over_hover.open()
        result = menu_over_hover.check_dropdown()
        assert str(result)


class TestCornerMenu:

    def test_corner_menu(self, driver):
        corner_menu = CornerMenuPage(driver, 'https://marshal.ru/')
        corner_menu.open()
        corner_menu.check_corner_menu()



