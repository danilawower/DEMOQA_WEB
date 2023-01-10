import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage


class TestElements:  #весь раздел элементов
    class TestTextBox: #раздел текст бокса

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")  #тут подтягиваем текстБоксПейдж из элементс_пейдж в которой подтянуты локаторы, видимости
            text_box_page.open()
            text_box_page.fill_all_fields() #здесь добавляем метод с текстБоксПейджа где заполняем данными поля
            text_box_page.check_filled_form() #проверить чек филд и спринтить ретёрны из элемент пейджа
            print(text_box_page.check_filled_form())

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()


    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button()
            #radio_button_page.click_on_the_radio_button('yes')
            #radio_button_page.click_on_the_radio_button('no')
            #radio_button_page.click_on_the_radio_button('impressive')


    class TestWebTable:
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            print(new_person)
            print(table_result)
            assert new_person in table_result







