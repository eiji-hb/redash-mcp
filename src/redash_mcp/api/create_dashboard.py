"""Redash create_dashboard API."""

from typing import Any

import httpx


class CreateDashboardClient:
    """Client for create_dashboard API."""

    def __init__(self, base_url: str, api_key: str, timeout: float = 30.0, verify_ssl: bool = True) -> None:
        self.base_url = base_url.rstrip("/")
        self._client = httpx.AsyncClient(
            base_url=self.base_url,
            headers={"Authorization": f"Key {api_key}"},
            timeout=timeout,
            verify=verify_ssl,
        )

    async def close(self) -> None:
        await self._client.aclose()

    async def execute(self, name: str) -> dict[str, Any]:
        """Create a new dashboard.

        Args:
            name: Name of the dashboard

        Returns:
            Created dashboard object
        """
        data = {"name": name}
        response = await self._client.post("/api/dashboards", json=data)
        response.raise_for_status()
        return response.json()
