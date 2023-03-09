import time

from pages.widgets_page2 import AccordianPage, AutocompletePage, SliderPage, ProgressbarPage, TabsPage, ToolTipsPage


class TestWidgets:

    class TestAccordian:
        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
            accordian_page.open()
            accordian_page.check_accordian('first')
            accordian_page.check_accordian('second')
            accordian_page.check_accordian('third')


    class TestAutocomplete:
        def test_autocomplete(self, driver):
            autocomplete_page = AutocompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            autocomplete_page.check_multiple_color()
            autocomplete_page.delete_multi()
            autocomplete_page.check_single_color()



    class TestSlider:
        def test_slider(self, driver):
            slider_page = SliderPage(driver, 'https://demoqa.com/slider')
            slider_page.open()
            after, before = slider_page.check_slider()
            assert after != before


    class TestProgressbar:
        def test_progressbar(self, driver):
            progressbar_page = ProgressbarPage(driver, 'https://demoqa.com/progress-bar')
            progressbar_page.open()
            after, before = progressbar_page.check_progressbar()
            assert after != before


    class TestTabs:
        def test_tabs(self, driver):
            tabs_page = TabsPage(driver, "https://demoqa.com/tabs")
            tabs_page.open()
            tabs_page.check_tabs('use')
            tabs_page.check_tabs('origin')
            tabs_page.check_tabs('what')
            tabs_page.check_random_tab()


    class TestToolTip:
        def test_tooltip(self, driver):
            tooltip_page = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
            tooltip_page.open()
            text = tooltip_page.check_tooltip()
            assert text == 'You hovered over the Button'


