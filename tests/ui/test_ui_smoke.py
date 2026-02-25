import pytest
from playwright.sync_api import sync_playwright, expect
from src.config import BASE_UI_URL

pytestmark = [pytest.mark.ui, pytest.mark.smoke]


def test_todomvc_add_item():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to app
        page.goto(BASE_UI_URL)

        # Add a todo item
        page.get_by_placeholder("What needs to be done?").fill("write first ui test")
        page.keyboard.press("Enter")

        # Assert the new item appears
        expect(page.get_by_test_id("todo-title")).to_contain_text("write first ui test")

        browser.close()