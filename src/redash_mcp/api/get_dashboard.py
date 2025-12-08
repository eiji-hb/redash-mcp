"""Redash get_dashboard API."""

from typing import Any

import httpx


class GetDashboardClient:
    """Client for get_dashboard API."""

    def __init__(self, base_url: str, api_key: str, timeout: float = 30.0) -> None:
        self.base_url = base_url.rstrip("/")
        self._client = httpx.AsyncClient(
            base_url=self.base_url,
            headers={"Authorization": f"Key {api_key}"},
            timeout=timeout,
        )

    async def close(self) -> None:
        await self._client.aclose()

    async def execute(self, dashboard_slug: str) -> dict[str, Any]:
        """Get a dashboard by slug.

        Args:
            dashboard_slug: Slug of the dashboard

        Returns:
            Dashboard object
        """
        response = await self._client.get(f"/api/dashboards/{dashboard_slug}")
        response.raise_for_status()
        return response.json()
