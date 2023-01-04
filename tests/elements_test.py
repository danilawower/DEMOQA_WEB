from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")  #тут подтягиваем текстБоксПейдж из элементс_пейдж в которой подтянуты локаторы, видимости
            text_box_page.open()
            text_box_page.fill_all_fields() #здесь добавляем метод с текстБоксПейджа где заполняем данными поля
            text_box_page.check_filled_form() #проверить чек филд и спринтить ретёрны из элемент пейджа
            print(text_box_page.check_filled_form())




