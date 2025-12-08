"""Redash archive_query API."""

from typing import Any

import httpx


class ArchiveQueryClient:
    """Client for archive_query API."""

    def __init__(self, base_url: str, api_key: str, timeout: float = 30.0) -> None:
        self.base_url = base_url.rstrip("/")
        self._client = httpx.AsyncClient(
            base_url=self.base_url,
            headers={"Authorization": f"Key {api_key}"},
            timeout=timeout,
        )

    async def close(self) -> None:
        await self._client.aclose()

    async def execute(self, query_id: int) -> dict[str, Any]:
        """Archive a query.

        Args:
            query_id: ID of the query to archive

        Returns:
            Response from the API
        """
        response = await self._client.delete(f"/api/queries/{query_id}")
        response.raise_for_status()
        if response.content:
            return response.json()
        return {"success": True, "query_id": query_id}
