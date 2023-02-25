import random
import time

from generator.generator import generated_person, generated_site_type
from locators.makeitmax_locators import MainPageLocators, LoginLogoutLocators, ProfilePageLocators, \
    FirsStepScenarioLocators
from locators.marshal_locators import PersonalAccountLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    locators = MainPageLocators()

    def check_main_page_registration(self):
        person = next(generated_person())
        self.element_is_clickable(self.locators.START_BUTTON).click()
        email = self.element_is_clickable(self.locators.EMAIL_FIELD)
        email.send_keys(person.email)
        self.element_is_clickable(self.locators.CHOICE_BUSINESS).click()
        business_list = self.elements_are_present(self.locators.BUSINESS_LIST)
        count = 15
        while count != 0:
            item = business_list[random.randint(1, 1)]
            if count > 0:
                self.go_to_element(item)
                item.click()
            break

        password = self.element_is_visible(self.locators.PASSWORD_FIELD)
        password.send_keys('132Test')
        password_repeat = self.element_is_visible(self.locators.PASSWORD_REPEAT_FIELD)
        password_repeat.send_keys('132Test')
        self.element_is_clickable(self.locators.CHECKBOX).click()
        self.element_is_clickable(self.locators.ACCEPT_BUTTON).click()
        self.element_is_clickable(self.locators.REGISTRATION_SUCCESS_BUTTON).click()


class MainPageLogin(BasePage):
    locators = LoginLogoutLocators()

    def check_login_logout(self):
        self.login_into_makeitmax()
        self.element_is_clickable(self.locators.MY_PROFILE).click()
        self.element_is_clickable(self.locators.PROFILE_LOGOUT_BUTTON).click()


class ProfilePage(BasePage):
    locators = ProfilePageLocators()

    def check_change_profile(self):
        person = next(generated_person())
        self.login_into_makeitmax()
        self.element_is_clickable(self.locators.MY_PROFILE).click()
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(person.firstname)
        self.element_is_visible(self.locators.PHONE_FIELD).send_keys(person.mobile)
        self.element_is_visible(self.locators.EMAIL_PROFILE_FIELD).send_keys(person.email)
        self.element_is_clickable(self.locators.SAVE_CHANGES_BUTTON).click()
        time.sleep(5)



class FirsStepScenario(BasePage):
    locators = FirsStepScenarioLocators

    def check_first_scenario(self):
        person = next(generated_person())
        self.login_into_makeitmax()
        self.element_is_clickable(self.locators.ZAPUSK_KOMPANII_BUTTON).click()
        self.element_is_clickable(self.locators.NEXT_BUTTON).click()
        self.element_is_visible(self.locators.NAME_PLACEHOLDER).send_keys(person.firstname)
        self.element_is_clickable(self.locators.NEXT_BUTTON).click()
        self.element_is_clickable(self.locators.MOBILE_PHONE_BUTTON).click()
        self.element_is_clickable(self.locators.MOBILE_PHONE_FIELD).send_keys(person.mobile)
        self.element_is_clickable(self.locators.NEXT_BUTTON).click()
        self.element_is_clickable(self.locators.NEXT_BUTTON).click()
        self.element_is_clickable(self.locators.BRAND_NAME_FIELD).send_keys(person.department)
        self.element_is_clickable(self.locators.NEXT_BUTTON).click()
        self.element_is_clickable(self.locators.COMPANY_NAME_FIELD).send_keys(person.department)
        self.element_is_clickable(self.locators.NEXT_BUTTON).click()
        random.sample(self.elements_are_visible(self.locators.BUSINESS_TYPE), k=1)[0].click()
        self.element_is_clickable(self.locators.NEXT_BUTTON).click()
        random.sample(self.elements_are_visible(self.locators.BUSINESS_RADIOBUTTON), k=1)[0].click()
        self.element_is_clickable(self.locators.NEXT_BUTTON).click()
        business_checkbox = self.elements_are_visible(self.locators.BUSINESS_CHECKBOX)
        random.sample(business_checkbox, k=1)[0].click()
        self.element_is_clickable(self.locators.NEXT_BUTTON).click()
        random.sample(self.elements_are_visible(self.locators.BUSINESS_CHECKBOX2), k=1)[0].click()
        self.element_is_clickable(self.locators.NEXT_BUTTON).click()
        self.element_is_clickable(self.locators.NEXT_BUTTON_WEBSITE).click()
        site = random.sample(next(generated_site_type()).site_type, k=1)
        self.element_is_visible(self.locators.WEBSITE_FIELD).send_keys(site)
        self.element_is_clickable(self.locators.NEXT_BUTTON).click()
        random.sample(self.elements_are_visible(self.locators.VK_FB_INS), k=1)[0].click()
        self.element_is_clickable(self.locators.NEXT_BUTTON).click()
        self.element_is_visible(self.locators.VK_FIELD).send_keys(site)
        self.element_is_clickable(self.locators.NEXT_BUTTON).click()


    def check_first_scenario2(self): #ПРОВЕРИТЬ СТРАНИЦУ ПЕРЕШЛ ЛИ НА ШАГ
        person = next(generated_person())
        self.login_into_makeitmax()
        self.element_is_clickable(self.locators.ZAPUSK_KOMPANII_BUTTON).click()
        step = self.element_is_visible(self.locators.STEP_COUNTER)


