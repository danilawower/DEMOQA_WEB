import random
import time

from generator.generator import generated_person
from locators.marshal_locators import PersonalAccountLocators, RegistrationLocators, ChangePersonalInformationLocators, \
    ProductCatalogLocators, MenuHoverOverPageLocators, CornerMenuLocators
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    locators = RegistrationLocators()

    def check_registration(self):
        person = next(generated_person())
        self.element_is_clickable(self.locators.REGISTRATION).click()
        self.element_is_clickable(self.locators.PHYS_LICO).click()
        self.element_is_clickable(self.locators.CONTINUE).click()
        self.element_is_visible(self.locators.EMAIL_FIELD).send_keys(person.email)
        self.element_is_visible(self.locators.PASSWORD_FIELD).send_keys('132546Da')
        self.element_is_visible(self.locators.PASSWORD_CONFIRMATION).send_keys('132546Da')
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(person.firstname)
        self.element_is_visible(self.locators.SURNAME_FIELD).send_keys(person.lastname)
        self.element_is_visible(self.locators.SURNAME2_FIELD).send_keys(person.lastname)
        self.element_is_visible(self.locators.PHONE_NUMBER).send_keys(person.mobile)
        self.element_is_visible(self.locators.INDEX_FIELD).send_keys(person.index)
        self.element_is_visible(self.locators.COUNTRY_FIELD).send_keys(person.country)
        self.element_is_clickable(self.locators.RULE1).click()
        self.element_is_clickable(self.locators.RULE2).click()
        self.element_is_clickable(self.locators.REGISTRATION_CONFIRM).click()
        logout = self.element_is_present(self.locators.LOGOUT_BUTTON).get_attribute("innerHTML").splitlines()[0]
        return logout


class PersonalAccountPage(BasePage):
    locators = PersonalAccountLocators()

    def check_login(self):
        self.element_is_clickable(self.locators.LOGIN_BUTTON).click()
        self.element_is_visible(self.locators.LOGIN_EMAIL_FIELD).send_keys('danilawower2@gmail.com')
        self.element_is_visible(self.locators.LOGIN_PASSWORD_FIELD).send_keys('132546Da')
        self.element_is_clickable(self.locators.LOGIN_ENTER).click()
        logout = self.element_is_present(self.locators.LOGOUT_BUTTON).get_attribute("innerHTML").splitlines()[
            0]  # взяли текст из кнопки
        return logout


class ChangePersonalInformationPage(BasePage):
    locators = ChangePersonalInformationLocators()


    def check_change_personal_info(self):
        person = next(generated_person())
        self.login_into()
        self.element_is_clickable(self.locators.MY_ACCOUNT_BUTTON).click()
        self.element_is_clickable(self.locators.CHANGE_INFO_BUTTON).click()
        new_surname = self.element_is_clickable(self.locators.SURNAME_FIELD)
        get_value_surname = new_surname.get_attribute('value')
        new_surname.clear()
        new_surname.send_keys(person.lastname)
        self.element_is_clickable(self.locators.SAVE_BUTTON).click()
        return person.lastname, get_value_surname



class ProductCatalogPage(BasePage):
    locators = ProductCatalogLocators()

    def check_product_menu(self):
        self.element_is_clickable(self.locators.PRODUCT_CATALOG).click()
        self.element_is_clickable(self.locators.MASLA).click()
        self.element_is_clickable(self.locators.MOTORNIE_MASLA).click()

        item_list = self.elements_are_present(self.locators.PROIZVODITEL_LIST)
        count = 164
        while count != 0:
            item = item_list[random.randint(5, 20)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break
        self.element_is_clickable(self.locators.BUTTON_SHOW).click()



class MenuHoverOverPage(BasePage):
    locators = MenuHoverOverPageLocators()

    def check_dropdown(self):
        dropdown = self.element_is_present(self.locators.CLIENTAM)
        self.action_move_to_element(dropdown)
        sub_menu = {'Blog': self.locators.BLOG, 'Novosti': self.locators.NOVOSTI, 'OKompanii': self.locators.O_KOMPANII,
                    'Kontakty': self.locators.KONTAKTY}
        self.element_is_visible(random.choice(list(sub_menu.values()))).click()
        text = self.element_is_visible(self.locators.H1).text
        return text


class CornerMenuPage(BasePage):
    locators = CornerMenuLocators()

    def check_corner_menu(self):
        self.login_into()
        self.element_is_clickable(self.locators.MAIN_BUTTON).click()
        menu = random.sample(self.elements_are_visible(self.locators.ELEMENTS), k=1)[0].click()








































