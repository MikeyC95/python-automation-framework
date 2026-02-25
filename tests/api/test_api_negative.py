import pytest

pytestmark = [pytest.mark.api, pytest.mark.smoke]


def test_posts_invalid_id_returns_404(api):
    response = api.get("/posts/0")
    assert response.status_code == 404


def test_nonexistent_route_returns_404(api):
    response = api.get("/this-route-should-not-exist")
    assert response.status_code == 404