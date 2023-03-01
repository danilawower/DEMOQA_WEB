from pages.elements_page2 import TextBoxPage, CheckBoxPage, RadioButtonPage


class TestElements:

    class TestTextBox:

        def test_textbox(self, driver):
            textbox_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            textbox_page.open()
            textbox_page.check_textbox()



    class TestCheckBox:

        def test_checkbox(self, driver):
            checkbox_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            checkbox_page.open()
            checkbox_page.check_checkbox()




    class TestRadioButton:

        def test_radiobutton(self, driver):
            radiobutton_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radiobutton_page.open()
            radiobutton_page.check_radiobutton('yes')
            radiobutton_page.check_radiobutton('impressive')
