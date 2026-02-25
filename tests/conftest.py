import pytest
from src.api.client import ApiClient
from src.config import BASE_API_URL


@pytest.fixture(scope="session")
def api():
    return ApiClient(BASE_API_URL)