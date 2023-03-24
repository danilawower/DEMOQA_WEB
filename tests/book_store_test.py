import time

from pages.book_store_page import BookStoreLoginPage


class TestBookStore:

    class TestBookStoreLogin:
        def test_login(self, driver):
            login_page = BookStoreLoginPage(driver, "https://demoqa.com/login")
            login_page.open()
            login_page.commit_login()
