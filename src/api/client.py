from __future__ import annotations

import requests
from typing import Any, Optional


class ApiClient:
    def __init__(
        self,
        base_url: str,
        timeout_s: int = 30,
        headers: Optional[dict[str, str]] = None,
    ):
        self.base_url = base_url.rstrip("/")
        self.timeout_s = timeout_s
        self.session = requests.Session()
        if headers:
            self.session.headers.update(headers)

    def request(self, method: str, path: str, **kwargs) -> requests.Response:
        """
        Generic request method so tests can call any HTTP verb.
        Example: api.request("GET", "/posts/1")
        """
        url = f"{self.base_url}/{path.lstrip('/')}"
        return self.session.request(method=method, url=url, timeout=self.timeout_s, **kwargs)

    def get(self, path: str, **kwargs) -> requests.Response:
        return self.request("GET", path, **kwargs)

    def post(self, path: str, **kwargs) -> requests.Response:
        return self.request("POST", path, **kwargs)

    def put(self, path: str, **kwargs) -> requests.Response:
        return self.request("PUT", path, **kwargs)

    def delete(self, path: str, **kwargs) -> requests.Response:
        return self.request("DELETE", path, **kwargs)


def assert_status(resp: requests.Response, expected: int) -> None:
    """
    Small helper so failures show useful context in CI.
    """
    body_preview = (resp.text or "")[:500]
    assert resp.status_code == expected, (
        f"Expected status {expected}, got {resp.status_code}. "
        f"URL: {resp.url}. "
        f"Body (first 500 chars): {body_preview}"
    )