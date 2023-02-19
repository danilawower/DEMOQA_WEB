import random
import time
from selenium.webdriver.common.keys import Keys

from generator.generator import generated_person, generated_car
from locators.marshal_locators import PersonalAccountLocators, RegistrationLocators, ChangePersonalInformationLocators, \
    ProductCatalogLocators, MenuHoverOverPageLocators, CornerMenuLocators, CarDropDownPageLocators, \
    ProductCatalogNewTabLocators, VinSearchLocators, MainBannerLocators
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

    def check_product_catalog(self):
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



class CarDropDownPage(BasePage):
    locators = CarDropDownPageLocators()

    def check_dropdown_car_auto_choice(self):
        self.element_is_clickable(self.locators.CAR_MARK_BUTTON).click()
        random.sample(self.elements_are_present(self.locators.CAR_MARK_LOCATOR), k=1)[0].click()
        car_title = self.element_is_present(self.locators.CAR_TITLE).get_attribute('title')
        self.element_is_clickable(self.locators.CAR_MODEL_BUTTON).click()
        random.sample(self.elements_are_present(self.locators.CAR_MODEL_LOCATOR), k=1)[0].click()
        self.element_is_clickable(self.locators.CAR_PRESENTATION_BUTTON).click()
        self.element_is_clickable(self.locators.SEARCH_BUTTON).click()
        text = self.element_is_present(self.locators.H1).text
        return text, car_title

    def check_dropdown_car_type_choice(self):
        car_mark = random.sample(next(generated_car()).car_name, k=1)
        self.element_is_clickable(self.locators.CAR_MARK_BUTTON).click()
        car_mark_field = self.element_is_visible(self.locators.CAR_MARK_FIELD)
        car_mark_field.send_keys(car_mark)
        car_mark_field.send_keys(Keys.ENTER)
        car_title = self.element_is_present(self.locators.CAR_TITLE).get_attribute('title')
        self.element_is_clickable(self.locators.CAR_MODEL_BUTTON).click()
        car_model_field = self.element_is_visible(self.locators.CAR_MODEL_FIELD)
        car_model_field.send_keys(random.randint(1, 3))
        car_model_field.send_keys(Keys.ENTER)
        self.element_is_clickable(self.locators.SEARCH_BUTTON).click()
        text = self.element_is_present(self.locators.H1).text
        return car_title, text



class ProductCatalogNewTabPage(BasePage):
    locators = ProductCatalogNewTabLocators()

    def check_product_catalog_new_tab(self):
        menu_list = self.elements_are_visible(self.locators.MENU)
        for item in menu_list:
            self.action_open_new_tab(item)
        self.driver.switch_to.window(self.driver.window_handles[1])
        text1 = self.element_is_present(self.locators.H1).text
        self.driver.switch_to.window(self.driver.window_handles[2])
        text2 = self.element_is_present(self.locators.H1).text
        self.driver.switch_to.window(self.driver.window_handles[3])
        text3 = self.element_is_present(self.locators.H1).text
        self.driver.switch_to.window(self.driver.window_handles[4])
        text4 = self.element_is_present(self.locators.H1).text
        self.driver.switch_to.window(self.driver.window_handles[5])
        text5 = self.element_is_present(self.locators.H1).text
        return text1, text2, text3, text4, text5


class VinSearchPage(BasePage):
    locators = VinSearchLocators()

    def check_vin_search(self):
        self.element_is_visible(self.locators.VIN_FIELD).send_keys(random.randint(1000, 99999))
        self.element_is_clickable(self.locators.VIN_SEARCH).click()
        random.sample(self.elements_are_visible(self.locators.VIN_ELEMENTS), k=1)[0].click()
        random.sample(self.elements_are_visible(self.locators.CAR_NAME), k=1)[0].click()
        random.sample(self.elements_are_visible(self.locators.CAR_CLASS), k=1)[0].click()




class MainBannerPage(BasePage):
    locators = MainBannerLocators()

    def check_main_banner(self):
        first_button = self.element_is_clickable(self.locators.FIRST_BUTTON)
        self.action_open_new_tab(first_button)
        self.element_is_clickable(self.locators.SECOND_ROUND_BUTTON).click()
        second_button = self.element_is_clickable(self.locators.SECOND_BUTTON)
        self.action_open_new_tab(second_button)
        self.driver.switch_to.window(self.driver.window_handles[1])
        text = self.element_is_present(self.locators.H1).text
        self.driver.switch_to.window(self.driver.window_handles[2])
        text2 = self.element_is_present(self.locators.H1).text
        return text, text2












































