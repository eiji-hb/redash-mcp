"""Redash create_query API."""

from typing import Any

import httpx


class CreateQueryClient:
    """Client for create_query API."""

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
        name: str,
        query: str,
        data_source_id: int,
        description: str | None = None,
    ) -> dict[str, Any]:
        """Create a new query.

        Args:
            name: Query name
            query: SQL query string
            data_source_id: ID of the data source to run this query against
            description: Optional query description

        Returns:
            Created query object
        """
        payload: dict[str, Any] = {
            "name": name,
            "query": query,
            "data_source_id": data_source_id,
        }
        if description is not None:
            payload["description"] = description

        response = await self._client.post("/api/queries", json=payload)
        response.raise_for_status()
        return response.json()
