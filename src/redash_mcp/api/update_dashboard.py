"""Redash update_dashboard API."""

from typing import Any

import httpx


class UpdateDashboardClient:
    """Client for update_dashboard API."""

    def __init__(self, base_url: str, api_key: str, timeout: float = 30.0) -> None:
        self.base_url = base_url.rstrip("/")
        self._client = httpx.AsyncClient(
            base_url=self.base_url,
            headers={"Authorization": f"Key {api_key}"},
            timeout=timeout,
        )

    async def close(self) -> None:
        await self._client.aclose()

    async def execute(self, dashboard_id: int, name: str | None = None) -> dict[str, Any]:
        """Update an existing dashboard.

        Args:
            dashboard_id: ID of the dashboard to update
            name: New name for the dashboard (optional)

        Returns:
            Updated dashboard object
        """
        data: dict[str, Any] = {}
        if name is not None:
            data["name"] = name
        response = await self._client.post(f"/api/dashboards/{dashboard_id}", json=data)
        response.raise_for_status()
        return response.json()
