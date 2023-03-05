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





