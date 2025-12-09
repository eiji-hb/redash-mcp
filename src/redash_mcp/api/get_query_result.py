"""Redash get_query_result API."""

from typing import Any

import httpx


class GetQueryResultClient:
    """Client for get_query_result API."""

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

    async def execute(self, query_id: int) -> dict[str, Any]:
        """Get cached result for a query.

        Args:
            query_id: ID of the query

        Returns:
            Query result data

        Note:
            Only works for non-parameterized queries.
        """
        response = await self._client.get(f"/api/queries/{query_id}/results")
        response.raise_for_status()
        return response.json()
