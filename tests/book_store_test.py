
from pages.book_store_page import LoginBookStorePage, RegisterNewUserPage, CheckBookAddingPage, \
    CheckBookDeletePage, CheckMyBooksPage


class TestBookStore:

    class TestBookStoreLogin:
        def test_login(self, driver):
            login_page = LoginBookStorePage(driver, "https://demoqa.com/login")
            login_page.open()
            login_page.commit_login()

    class TestRegisterNewUser:
        def test_register_new_user(self, driver):
            login_page = RegisterNewUserPage(driver, "https://demoqa.com/login")
            login_page.open()
            login_page.register_new_user()



    class TestBookAdding:
        def test_book_adding(self, driver):
            login_page = CheckBookAddingPage(driver, "https://demoqa.com/login")
            login_page.open()
            login_page.check_book_adding()


    class TestBookDelete:
        def test_book_delete(self, driver):
            login_page = CheckBookDeletePage(driver, "https://demoqa.com/login")
            login_page.open()
            login_page.delete_book()


    class TestMyBooks:
        def test_my_book(self, driver):
            login_page = CheckMyBooksPage(driver, "https://demoqa.com/login")
            login_page.open()
            before, after = login_page.check_my_books()
            assert before == after
