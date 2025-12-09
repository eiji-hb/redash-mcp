"""Redash update_query API."""

from typing import Any

import httpx


class UpdateQueryClient:
    """Client for update_query API."""

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

    async def execute(
        self,
        query_id: int,
        name: str | None = None,
        query: str | None = None,
        data_source_id: int | None = None,
        description: str | None = None,
    ) -> dict[str, Any]:
        """Update an existing query.

        Args:
            query_id: ID of the query to update
            name: New query name
            query: New SQL query string
            data_source_id: New data source ID
            description: New description

        Returns:
            Updated query object
        """
        payload: dict[str, Any] = {}
        if name is not None:
            payload["name"] = name
        if query is not None:
            payload["query"] = query
        if data_source_id is not None:
            payload["data_source_id"] = data_source_id
        if description is not None:
            payload["description"] = description

        response = await self._client.post(f"/api/queries/{query_id}", json=payload)
        response.raise_for_status()
        return response.json()
