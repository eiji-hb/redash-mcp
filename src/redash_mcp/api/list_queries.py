"""Redash list_queries API."""

from typing import Any

import httpx


class ListQueriesClient:
    """Client for list_queries API."""

    def __init__(self, base_url: str, api_key: str, timeout: float = 30.0) -> None:
        """Initialize client.

        Args:
            base_url: Redash instance URL
            api_key: Redash API key
            timeout: Request timeout in seconds
        """
        self.base_url = base_url.rstrip("/")
        self._client = httpx.AsyncClient(
            base_url=self.base_url,
            headers={"Authorization": f"Key {api_key}"},
            timeout=timeout,
        )

    async def close(self) -> None:
        """Close the HTTP client."""
        await self._client.aclose()

    async def execute(self, page: int = 1, page_size: int = 25) -> dict[str, Any]:
        """List all queries.

        Args:
            page: Page number
            page_size: Number of results per page

        Returns:
            List of queries with pagination info
        """
        response = await self._client.get(
            "/api/queries", params={"page": page, "page_size": page_size}
        )
        response.raise_for_status()
        return response.json()
