import time

from pages.form_page2 import FormPage


class TestForm:
    def test_form(self, driver):
        form_page = FormPage(driver, "https://demoqa.com/automation-practice-form")
        form_page.open()
        form_page.fill_form()
        time.sleep(3)




