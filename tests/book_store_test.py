import allure

from pages.book_store_page import LoginBookStorePage, RegisterNewUserPage, CheckBookAddingPage, \
    CheckBookDeletePage, CheckMyBooksPage


@allure.suite('Book Store')
class TestBookStore:

    @allure.feature('New user')
    class TestRegisterNewUser:

        @allure.title('Check new user registration')
        def test_register_new_user(self, driver):
            login_page = RegisterNewUserPage(driver, "https://demoqa.com/login")
            login_page.open()
            login_page.register_new_user()

    @allure.feature('Login')
    class TestBookStoreLogin:

        @allure.title('Check login')
        def test_login(self, driver):
            login_page = LoginBookStorePage(driver, "https://demoqa.com/login")
            login_page.open()
            login_page.commit_login()

    @allure.feature('Book adding')
    class TestBookAdding:

        @allure.title('Check book adding')
        def test_book_adding(self, driver):
            login_page = CheckBookAddingPage(driver, "https://demoqa.com/login")
            login_page.open()
            login_page.check_book_adding()


    @allure.feature('My books')
    class TestMyBooks:

        @allure.title('Check my books')
        def test_my_book(self, driver):
            login_page = CheckMyBooksPage(driver, "https://demoqa.com/login")
            login_page.open()
            before, after = login_page.check_my_books()
            assert before == after


    @allure.feature('Book delete')
    class TestBookDelete:

        @allure.title('Check book deleting')
        def test_book_delete(self, driver):
            login_page = CheckBookDeletePage(driver, "https://demoqa.com/login")
            login_page.open()
            login_page.delete_book()
