import pytest

pytestmark = [pytest.mark.api, pytest.mark.smoke]

def test_jsonplaceholder_posts_smoke(api):
    r = api.get("/posts/1")
    assert r.status_code == 200
    body = r.json()
    assert body["id"] == 1
    assert "title" in body