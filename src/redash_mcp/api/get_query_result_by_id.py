"""Redash get_query_result_by_id API."""

from typing import Any

import httpx


class GetQueryResultByIdClient:
    """Client for get_query_result_by_id API."""

    def __init__(self, base_url: str, api_key: str, timeout: float = 30.0) -> None:
        self.base_url = base_url.rstrip("/")
        self._client = httpx.AsyncClient(
            base_url=self.base_url,
            headers={"Authorization": f"Key {api_key}"},
            timeout=timeout,
        )

    async def close(self) -> None:
        await self._client.aclose()

    async def execute(self, query_result_id: int) -> dict[str, Any]:
        """Get a query result by its ID.

        Args:
            query_result_id: ID of the query result

        Returns:
            Query result data
        """
        response = await self._client.get(f"/api/query_results/{query_result_id}")
        response.raise_for_status()
        return response.json()
