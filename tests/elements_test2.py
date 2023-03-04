import time

from pages.elements_page2 import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    UploadDownloadPage, DynamicPropertiesPage


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


    class TestWebTables:

        def test_web_table(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person, check = web_table_page.check_new_person()
            assert new_person in check


    class TestButtons:

        def test_buttons(self, driver):
            buttons_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            buttons_page.open()
            buttons_page.check_buttons('right')
            buttons_page.check_buttons('double')
            buttons_page.check_buttons('click')



    class TestLinks:

        def test_links(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            home_link = links_page.click_home_link()
            dynamic_link = links_page.click_dynamic_link()
            forbidden_link = links_page.click_forbidden_link()
            assert home_link == 'https://demoqa.com/'
            assert dynamic_link == 'https://demoqa.com/'
            assert forbidden_link == 403



    class TestUploadDownload:

        def test_download(self, driver):
            download_page = UploadDownloadPage(driver, "https://demoqa.com/upload-download")
            download_page.open()
            download_page.check_download()

        def test_upload(self, driver):
            download_page = UploadDownloadPage(driver, "https://demoqa.com/upload-download")
            download_page.open()
            download_page.check_upload()


    class TestDynamicPage:

        def test_visible_after(self, driver):
            dynamic_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            dynamic_page.open()
            dynamic_page.check_enable_after_button()

        def test_color_change(self, driver):
            dynamic_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            dynamic_page.open()
            before, after = dynamic_page.check_color_change()
            assert before != after