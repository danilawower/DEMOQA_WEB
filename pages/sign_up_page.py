from locators.locators import SignUpLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

class SignUpPage(BasePage):
    locators = SignUpLocators()

    def fill_email(self, mail_input):
        self.element_is_visible(self.locators.EMAIL_FIELD).send_keys(mail_input)

    def fill_pswds(self, passwrd_input):
        self.element_is_visible(self.locators.PASS_FIELD).send_keys(passwrd_input)
        self.element_is_visible(self.locators.CONF_FIELD).send_keys(passwrd_input)

    def choose_category(self):
        self.element_is_visible(self.locators.CHECK_BOX).click()
        self.element_is_visible(self.locators.DOWN_ARROW).click()
        self.element_is_visible(self.locators.CATEGORY).click()

    def submit_form(self):
        self.element_is_visible(self.locators.SUBMIT).click()

    def success(self):
        self.element_is_present(self.locators.SUCCESS_STR)

    def success_ok_btn(self):
        self.element_is_visible(self.locators.OK_BTN).click()

    def check_password_field(self):
        self.element_is_not_visible(self.locators.PASS_FIELD)

    def clear_mail(self):
        self.clear(self.locators.EMAIL_FIELD)

    def clear_password(self):
        self.clear(self.locators.PASS_FIELD)
        self.clear(self.locators.CONF_FIELD)

    def pass_eye_btn(self):
        self.element_is_visible(self.locators.PASS_EYE).click()

    def confirm_eye_btn(self):
        self.element_is_visible(self.locators.CON_EYE).click()

    def check_popup(self, popup_txt, timeout=5):
        wait(self.driver, timeout).until(EC.text_to_be_present_in_element(self.locators.SUCCESS_STR, popup_txt))

    def show_password(self, timeout=5):
        wait(self.driver, timeout).until(EC.text_to_be_present_in_element_attribute(self.locators.PASS_FIELD, "type", "text" ))

    def hidden_password(self, timeout=5):
        wait(self.driver, timeout).until(EC.text_to_be_present_in_element_attribute(self.locators.PASS_FIELD, "type", "password"))

    def show_confirm(self, timeout=5):
        wait(self.driver, timeout).until(EC.text_to_be_present_in_element_attribute(self.locators.CONF_FIELD, "type", "text" ))

    def hidden_confirm(self, timeout=5):
        wait(self.driver, timeout).until(EC.text_to_be_present_in_element_attribute(self.locators.CONF_FIELD, "type", "password"))

    def no_password_field(self):
        self.element_is_not_visible(self.locators.PASS_FIELD)

    def wrong_mail(self, timeout=5):
        wait(self.driver, timeout).until(EC.visibility_of_element_located(self.locators.ERROR_MAIL))

    def wrong_mail_msg(self):
      return self.element_is_visible(self.locators.ERROR_MAIL).text

    def disabled_reg_btn(self):
        self.element_is_not_clickable(self.locators.SUBMIT)

    def wrong_pswd(self, timeout=5):
        wait(self.driver, timeout).until(EC.visibility_of_element_located(self.locators.RED_LINE))

    def get_redline_border(self):
        return self.get_css(self.locators.RED_LINE, "border")

    def pswd_tooltip(self, timeout=5):
        self.element_is_visible(self.locators.PASS_FIELD).click()
        wait(self.driver, timeout).until(EC.visibility_of_element_located(self.locators.PASS_TOOLTIP))

    def check_filled_sign_up(self):
        email_text = self.get_text_from_attribute(self.locators.EMAIL_FIELD, "value")
        password_text = self.get_text_from_attribute(self.locators.PASS_FIELD, "value")
        confirm_text = self.get_text_from_attribute(self.locators.CONF_FIELD, "value")
        assert password_text == confirm_text
        return email_text, password_text

    def check_password_placeholder(self):
        password_placeholder = self.get_text_from_attribute(self.locators.PASS_FIELD, "placeholder")
        confirm_placeholder = self.get_text_from_attribute(self.locators.CONF_FIELD, "placeholder")
        return password_placeholder, confirm_placeholder





