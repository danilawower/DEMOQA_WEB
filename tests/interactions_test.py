from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DraggablePage


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


    class TestResizable:

        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            rez = resizable_page.change_size_resizable_box()
            print(rez)


    class TestDroppable:

        def test_simple(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text = droppable_page.drop_simple()
            assert text == "Dropped!"

        def test_acceptable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            accept, not_accept = droppable_page.drop_accept()
            assert accept != not_accept

        def test_prevent(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            not_greedy, not_greedy_inner, greedy, greedy_inner = droppable_page.drop_prevent()
            print(not_greedy)
            print(not_greedy_inner)
            print(greedy)
            print(greedy_inner)

        def test_revert(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            droppable_page.drop_revert('will')
            droppable_page.drop_revert('not_will')


    class TestDraggablePage:

        def test_simple_drag(self, driver):
            draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable_page.open()
            before_position, after_position = draggable_page.simple_dra_box()
            assert before_position != after_position


