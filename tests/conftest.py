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
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()