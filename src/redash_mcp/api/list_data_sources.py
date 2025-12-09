"""Redash list_data_sources API."""

from typing import Any

import httpx


class ListDataSourcesClient:
    """Client for list_data_sources API."""

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

    async def execute(self) -> list[dict[str, Any]]:
        """List all data sources.

        Returns:
            List of data source objects
        """
        response = await self._client.get("/api/data_sources")
        response.raise_for_status()
        return response.json()
