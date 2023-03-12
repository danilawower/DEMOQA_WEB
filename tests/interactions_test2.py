import time

from pages.interactions_page2 import SortablePage, SelectablePage, ResizablePage, DroppablePage


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


    class TestDroppable:
        def test_droppable_simple(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            result = droppable_page.check_droppable_simple()
            assert result == 'Dropped!'

        def test_droppable_accept(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            result_not_accept, result_accept = droppable_page.check_droppable_accept()
            assert result_not_accept == 'Drop here'
            assert result_accept == 'Dropped!'

