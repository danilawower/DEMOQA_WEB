import random

from selenium.webdriver import Keys

from generator.generator import generated_person, generated_subject
from locators.form_page_locators2 import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):
    locators = FormPageLocators()

    def fill_form(self):
        person = next(generated_person())
        self.element_is_present(self.locators.NAME_FIELD).send_keys(person.firstname)
        self.element_is_present(self.locators.LASTNAME_FIELD).send_keys(person.lastname)
        self.element_is_present(self.locators.EMAIL_FIELD).send_keys(person.email)
        gender = self.elements_are_present(self.locators.GENDER_RADIO)
        random.sample(gender, k=1)[0].click()
        self.element_is_present(self.locators.MOBILE_FIELD).send_keys(person.mobile)
        date = self.element_is_present(self.locators.DATE_FIELD)
        date.click()
        date_pick = self.elements_are_present(self.locators.DATE_PICK)
        random.sample(date_pick, k=1)[0].click()
        subject = random.sample(next(generated_subject()).subject_name, k=1)
        subject_input = self.element_is_clickable(self.locators.SUBJECTS)
        subject_input.send_keys(subject)
        subject_input.send_keys(Keys.ENTER)
        hobbies = self.elements_are_present(self.locators.CHECKBOX)
        random.sample(hobbies, k=1)[0].click()
        upload_button = self.element_is_clickable(self.locators.UPLOAD_BUTTON)
        path = 'C:\\Users\\daniil\\Desktop\\python\\Screenshot_1.jpg'
        upload_button.send_keys(path)
        self.element_is_present(self.locators.CURRENT_ADDRESS).send_keys(person.current_address)
        self.element_is_clickable(self.locators.STATE).click()
        self.element_is_clickable(self.locators.STATE_INPUT).send_keys(Keys.ENTER)
        self.element_is_clickable(self.locators.CITY).click()
        self.element_is_clickable(self.locators.CITY_INPUT).send_keys(Keys.ENTER)
        self.element_is_clickable(self.locators.SUBMIT).click()





