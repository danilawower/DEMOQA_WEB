from pages.elements_page import TextBoxPage, CheckBoxPage


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





