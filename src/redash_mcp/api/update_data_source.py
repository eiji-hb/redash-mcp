"""Redash update_data_source API."""

from typing import Any

import httpx


class UpdateDataSourceClient:
    """Client for update_data_source API."""

    def __init__(self, base_url: str, api_key: str, timeout: float = 30.0) -> None:
        self.base_url = base_url.rstrip("/")
        self._client = httpx.AsyncClient(
            base_url=self.base_url,
            headers={"Authorization": f"Key {api_key}"},
            timeout=timeout,
        )

    async def close(self) -> None:
        await self._client.aclose()

    async def execute(
        self,
        data_source_id: int,
        name: str | None = None,
        options: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Update an existing data source.

        Args:
            data_source_id: ID of the data source to update
            name: New name for the data source (optional)
            options: New connection options (optional)

        Returns:
            Updated data source object
        """
        data: dict[str, Any] = {}
        if name is not None:
            data["name"] = name
        if options is not None:
            data["options"] = options
        response = await self._client.post(f"/api/data_sources/{data_source_id}", json=data)
        response.raise_for_status()
        return response.json()
