"""Redash execute_query API."""

from typing import Any

import httpx


class ExecuteQueryClient:
    """Client for execute_query API."""

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
        parameters: dict[str, Any] | None = None,
        max_age: int | None = None,
    ) -> dict[str, Any]:
        """Execute a query or get cached result.

        Args:
            query_id: ID of the query to execute
            parameters: Query parameters (for parameterized queries)
            max_age: Max cache age in seconds. Set to 0 to force fresh execution.

        Returns:
            Query result or job object if execution is in progress
        """
        payload: dict[str, Any] = {}
        if parameters is not None:
            payload["parameters"] = parameters
        if max_age is not None:
            payload["max_age"] = max_age

        response = await self._client.post(f"/api/queries/{query_id}/results", json=payload)
        response.raise_for_status()
        return response.json()
