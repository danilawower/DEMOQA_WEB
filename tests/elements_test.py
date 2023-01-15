import random
import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage


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
            assert new_person in table_result

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)] #ищем рандомный кейворд(данные опльзователя)
            web_table_page.search_some_person(key_word)
            table_result = web_table_page.check_search_person()
            assert key_word in table_result, "the person was not found in the table"


        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_some_person(lastname)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            print(age)
            print(row)
            assert lastname in row




    class TestButtonsPage:
        def test_different_click_on_the_buttons(self, driver):
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            double = button_page.click_on_different_button('double')
            right = button_page.click_on_different_button('right')
            click = button_page.click_on_different_button('click')
            assert double == 'You have done a double click'
            assert right == 'You have done a right click'
            assert click == 'You have done a dynamic click'



