import pytest
from src.ui.pages.todomvc_page import TodoMVCPage

pytestmark = [pytest.mark.ui, pytest.mark.smoke]


def test_todomvc_add_item(page):
    app = TodoMVCPage(page).open()
    app.add_item("write first ui test")
    app.assert_item_visible("write first ui test")

def test_toggle_todo_item(page):
    app = TodoMVCPage(page).open()

    app.add_item("complete me")
    app.toggle_first_item()
    app.assert_first_item_completed()