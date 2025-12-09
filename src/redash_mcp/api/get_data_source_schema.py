"""Redash get_data_source_schema API."""

from typing import Any

import httpx


class GetDataSourceSchemaClient:
    """Client for get_data_source_schema API."""

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

    async def execute(self, data_source_id: int, refresh: bool = False) -> dict[str, Any]:
        """Get schema for a data source.

        Args:
            data_source_id: ID of the data source
            refresh: Force refresh the schema cache (default: False)

        Returns:
            Schema object containing tables and columns
        """
        params = {}
        if refresh:
            params["refresh"] = "true"
        response = await self._client.get(f"/api/data_sources/{data_source_id}/schema", params=params)
        response.raise_for_status()
        return response.json()
