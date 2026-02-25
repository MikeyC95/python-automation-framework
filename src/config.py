import os

BASE_API_URL = os.getenv(
    "BASE_API_URL",
    "https://jsonplaceholder.typicode.com"
)

BASE_UI_URL = os.getenv(
    "BASE_UI_URL",
    "https://demo.playwright.dev/todomvc/"
)