
from pages.book_store_page import BookStorePage


class TestBookStore:

    class TestBookStoreLogin:
        def test_login(self, driver):
            login_page = BookStorePage(driver, "https://demoqa.com/login")
            login_page.open()
            login_page.commit_login()

        def test_register_new_user(self, driver):
            login_page = BookStorePage(driver, "https://demoqa.com/login")
            login_page.open()
            login_page.register_new_user()


        def test_book_adding(self, driver):
            login_page = BookStorePage(driver, "https://demoqa.com/login")
            login_page.open()
            login_page.check_book_adding()


        def test_book_delete(self, driver):
            login_page = BookStorePage(driver, "https://demoqa.com/login")
            login_page.open()
            login_page.delete_book()

        def test_my_book(self, driver):
            login_page = BookStorePage(driver, "https://demoqa.com/login")
            login_page.open()
            before, after = login_page.check_my_books()
            assert before == after
