from src.api.client import ApiClient

def test_jsonplaceholder_posts_smoke():
    api = ApiClient("https://jsonplaceholder.typicode.com")
    r = api.get("/posts/1")
    assert r.status_code == 200
    body = r.json()
    assert body["id"] == 1
    assert "title" in body