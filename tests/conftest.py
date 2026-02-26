import os
import pytest
from playwright.sync_api import sync_playwright

from src.api.client import ApiClient
from src.config import BASE_API_URL

# ---------- API fixtures ----------

@pytest.fixture(scope="session")
def api():
    return ApiClient(BASE_API_URL)

# ---------- UI fixtures ----------

HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"

@pytest.fixture()
def page(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS)
        context = browser.new_context()
        page = context.new_page()

        yield page

        # After test runs, check if it failed
        if request.node.rep_call.failed:
            os.makedirs("artifacts", exist_ok=True)
            screenshot_path = f"artifacts/{request.node.name}.png"
            page.screenshot(path=screenshot_path)
            print(f"\n📸 Screenshot saved to {screenshot_path}")

        context.close()
        browser.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)