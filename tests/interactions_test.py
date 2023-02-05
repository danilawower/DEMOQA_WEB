from pages.interactions_page import SortablePage, SelectablePage


class TestInteractions:


    class TestSortablePage:

        def test_sortable_page(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_grid_order()
            assert list_before != list_after
            assert grid_before != grid_after


    class TestSelectablePage:

        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            list_item = selectable_page.select_list_item()
            grid = selectable_page.select_grid_item()
            assert len(list_item) > 0
            assert len(grid) > 0

