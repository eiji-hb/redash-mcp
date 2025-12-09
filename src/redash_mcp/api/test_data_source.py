"""Redash test_data_source API."""

from typing import Any

import httpx


class TestDataSourceClient:
    """Client for test_data_source API."""

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

    async def execute(self, data_source_id: int) -> dict[str, Any]:
        """Test connection to a data source.

        Args:
            data_source_id: ID of the data source to test

        Returns:
            Test result object
        """
        response = await self._client.post(f"/api/data_sources/{data_source_id}/test")
        response.raise_for_status()
        return response.json()
