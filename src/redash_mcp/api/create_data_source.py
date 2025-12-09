"""Redash create_data_source API."""

from typing import Any

import httpx


class CreateDataSourceClient:
    """Client for create_data_source API."""

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

    async def execute(self, name: str, type: str, options: dict[str, Any]) -> dict[str, Any]:
        """Create a new data source.

        Args:
            name: Name of the data source
            type: Type of the data source (e.g., "pg", "mysql", "bigquery")
            options: Connection options for the data source

        Returns:
            Created data source object
        """
        data = {
            "name": name,
            "type": type,
            "options": options,
        }
        response = await self._client.post("/api/data_sources", json=data)
        response.raise_for_status()
        return response.json()
