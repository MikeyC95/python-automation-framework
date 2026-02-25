import pytest
from playwright.sync_api import sync_playwright
from src.ui.pages.todomvc_page import TodoMVCPage

pytestmark = [pytest.mark.ui, pytest.mark.smoke]


def test_todomvc_add_item():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        app = TodoMVCPage(page).open()
        app.add_item("write first ui test")
        app.assert_item_visible("write first ui test")

        browser.close()