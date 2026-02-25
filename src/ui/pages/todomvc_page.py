from playwright.sync_api import Page, expect
from src.config import BASE_UI_URL


class TodoMVCPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self) -> "TodoMVCPage":
        self.page.goto(BASE_UI_URL)
        return self

    def add_item(self, text: str) -> "TodoMVCPage":
        self.page.get_by_placeholder("What needs to be done?").fill(text)
        self.page.keyboard.press("Enter")
        return self

    def assert_item_visible(self, text: str) -> "TodoMVCPage":
        expect(self.page.get_by_test_id("todo-title")).to_contain_text(text)
        return self
    
    def toggle_first_item(self) -> "TodoMVCPage":
        self.page.locator(".todo-list li input.toggle").first.click()
        return self


    def assert_first_item_completed(self) -> "TodoMVCPage":
        expect(self.page.locator(".todo-list li").first).to_have_class("completed")
        return self