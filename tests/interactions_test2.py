import time

from pages.interactions_page2 import SortablePage, SelectablePage, ResizablePage


class TestInteractions:

    class TestSortable:
        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            sortable_page.check_sortable_list()
            sortable_page.check_sortable_grid()
            time.sleep(3)


    class TestSelectable:
        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            list_elements = selectable_page.check_selectable_list()
            grid_elements = selectable_page.check_selectable_grid()
            assert len(list_elements) > 0
            assert len(grid_elements) > 0


    class TestResizable:
        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            before, after = resizable_page.change_parameters()
            assert before != after
