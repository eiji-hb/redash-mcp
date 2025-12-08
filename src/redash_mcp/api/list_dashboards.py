"""Redash list_dashboards API."""

from typing import Any

import httpx


class ListDashboardsClient:
    """Client for list_dashboards API."""

    def __init__(self, base_url: str, api_key: str, timeout: float = 30.0) -> None:
        self.base_url = base_url.rstrip("/")
        self._client = httpx.AsyncClient(
            base_url=self.base_url,
            headers={"Authorization": f"Key {api_key}"},
            timeout=timeout,
        )

    async def close(self) -> None:
        await self._client.aclose()

    async def execute(self, page: int = 1, page_size: int = 25) -> dict[str, Any]:
        """List all dashboards.

        Args:
            page: Page number (default: 1)
            page_size: Number of results per page (default: 25)

        Returns:
            Paginated list of dashboard objects
        """
        params = {"page": page, "page_size": page_size}
        response = await self._client.get("/api/dashboards", params=params)
        response.raise_for_status()
        return response.json()
