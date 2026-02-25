import pytest

pytestmark = [pytest.mark.api, pytest.mark.smoke]

def test_jsonplaceholder_posts_smoke(api):
    response = api.get("/posts/1")
    assert response.status_code == 200
    body = response.json()
    assert body["id"] == 1
    assert "title" in body