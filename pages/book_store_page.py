import random
import time

import allure
from selenium.common import NoAlertPresentException
from selenium.webdriver import Keys

from generator.generator import generated_person
from locators.book_store_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginBookStorePage(BasePage):
    locators = LoginPageLocators()

    @allure.step('Go to Login page')
    def commit_login(self):
        with allure.step('Fill login field'):
            self.element_is_clickable(self.locators.LOGIN_FIELD).send_keys('username1')
        with allure.step('Fill password field'):
            self.element_is_present(self.locators.PASSWORD_FIELD).send_keys('@#wTmBpo4')
        with allure.step('Click login button'):
            self.element_is_clickable(self.locators.LOGIN_BUTTON).click()


class RegisterNewUserPage(BasePage):
    locators = LoginPageLocators()

    @allure.step('Go to Register page')
    def register_new_user(self):
        person = next(generated_person())
        with allure.step('Click new user button'):
            self.element_is_clickable(self.locators.NEW_USER_BUTTON).click()
        with allure.step('Enter first name'):
            self.element_is_present(self.locators.FIRST_NAME).send_keys(person.firstname)
        with allure.step('Enter last name and log pass'):
            self.element_is_present(self.locators.LAST_NAME).send_keys(person.lastname)
            self.element_is_present(self.locators.LOGIN_FIELD).send_keys(f'username{random.randint(1,15)}')
            self.element_is_present(self.locators.PASSWORD_FIELD).send_keys('@#wTmBpo4')
        #self.element_is_present(self.locators.CAPTCHA_CHECKBOX).click()
        #self.element_is_clickable(self.locators.REGISTER_BUTTON).click()



class CheckBookAddingPage(BasePage):
    locators = LoginPageLocators()

    def check_book_adding(self):
        self.commit_login()
        self.element_is_clickable(self.locators.GO_TO_STORE_BUTTON).click()
        book_list = self.elements_are_present(self.locators.BOOK_LIST)
        random.sample(book_list, k=1)[0].click()
        self.element_is_clickable(self.locators.ADD_NEW_BOOK).click()
        try:
            alert = self.driver.switch_to.alert()
            alert.accept()
        except NoAlertPresentException:
            print('exception handled')


class CheckBookDeletePage(BasePage):
    locators = LoginPageLocators()

    def delete_book(self):
        self.commit_login()
        self.element_is_clickable(self.locators.DELETE_BOOK).click()
        try:
            self.driver.switch_to.alert.accept()
        except NoAlertPresentException:
            print("exception handled")


class CheckMyBooksPage(BasePage):
    locators = LoginPageLocators()


    def take_name_of_book(self, element):
        book_text = element.get_attribute("innerHTML").splitlines()[0]
        split_text = book_text.split(' ')
        confirmation_num = split_text[2]
        return confirmation_num


    def check_my_books(self):
        self.commit_login()
        book_list = self.element_is_present(self.locators.BOOK_LIST)
        book_text_before = self.take_name_of_book(book_list)
        search_box = self.element_is_present(self.locators.SEARCH_BOX)
        search_box.send_keys(book_text_before)
        book_list = self.element_is_present(self.locators.BOOK_LIST)
        book_text_after = self.take_name_of_book(book_list)
        return book_text_before, book_text_after






