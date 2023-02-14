import time

from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderProgressBarPage, TabsPage, \
    ToolTipsPage, MenuPage


class TestWidgets:
    class TestAccordianPage:

        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
            accordian_page.open()
            first_title, first_content = accordian_page.check_accordian('first')
            second_title, second_content = accordian_page.check_accordian('second')
            third_title, third_content = accordian_page.check_accordian('third')
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0
            assert second_title == 'Where does it come from?' and second_content > 0
            assert third_title == 'Why do we use it?' and third_content > 0


    class TestAutoCompletePage:

        def test_remove_value_from_multi(self, driver):
            autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            after = autocomplete_page.fill_input_multi_autocomplete()
            before = autocomplete_page.remove_value_from_multi()
            assert after != before

        def test_multi_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            colors = autocomplete_page.fill_input_multi_autocomplete()
            colors_result = autocomplete_page.check_color_in_multi()
            assert colors == colors_result #в данном тесте я ввёл значения рандомные цвета(которые были текстом) и забрал в резалте color.text списком


        def test_single_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            color = autocomplete_page.fill_input_single()
            color_result = autocomplete_page.check_color_single()
            assert " " + color == color_result


    class TestDatePickerPage:

        def test_change_date(self, driver):
            date_picker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
            date_picker_page.open()
            date = date_picker_page.select_date()
            print(date)

        def test_change_date_and_time(self, driver):
            date_picker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
            date_picker_page.open()


    class TestSliderProgressBarPage:

        def test_slider_page(self, driver):
            slider_page = SliderProgressBarPage(driver, 'https://demoqa.com/slider')
            slider_page.open()
            value_before, value_after = slider_page.change_slider_value()
            assert value_before != value_after

        def test_progressbar(self, driver):
            slider_page = SliderProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            slider_page.open()
            after, before = slider_page.change_progress_bar()
            assert before != after

    class TestTabsPage:

        def test_tabs_page_list(self, driver):
            tabs_page = TabsPage(driver, "https://demoqa.com/tabs")
            tabs_page.open()
            what_button, what_content = tabs_page.check_tabs_list('what')
            use_button, use_content = tabs_page.check_tabs_list('use')
            origin_button, origin_content = tabs_page.check_tabs_list('origin')
            assert what_button, what_content != 0


    class TestToolTips:

        def test_tool_tip(self, driver):
            tooltips_page = ToolTipsPage(driver, "https://demoqa.com/tool-tips")
            tooltips_page.open()
            button_text, contrary_text, field_text, section_text = tooltips_page.check_tool_tips()
            #assert button_text == "You hovered over the Button"
            #assert contrary_text == "You hovered over the Contrary"
            #assert field_text == "You hovered over the text field"
            #assert section_text == "You hovered over the Button"
            print(button_text)
            print(contrary_text)
            print(field_text)
            print(section_text)


    class TestMenu:

        def test_menu(self, driver):
            menu_page = MenuPage(driver, 'https://demoqa.com/tool-tips')
            menu_page.open()
            data = menu_page.check_menu()
            time.sleep(5)
            assert data == ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1', 'Sub Sub Item 2', 'Main Item 3']