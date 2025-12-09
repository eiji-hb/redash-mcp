"""Redash list_data_source_types API."""

from typing import Any

import httpx


class ListDataSourceTypesClient:
    """Client for list_data_source_types API."""

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
        """List available data source types.

        Returns:
            List of data source type objects
        """
        response = await self._client.get("/api/data_sources/types")
        response.raise_for_status()
        return response.json()
