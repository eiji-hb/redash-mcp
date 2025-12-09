"""Redash get_query API."""

from typing import Any

import httpx


class GetQueryClient:
    """Client for get_query API."""

    def __init__(self, base_url: str, api_key: str, timeout: float = 30.0, verify_ssl: bool = True) -> None:
        """Initialize client.

        Args:
            base_url: Redash instance URL
            api_key: Redash API key
            timeout: Request timeout in seconds
            verify_ssl: Whether to verify SSL certificates
        """
        self.base_url = base_url.rstrip("/")
        self._client = httpx.AsyncClient(
            base_url=self.base_url,
            headers={"Authorization": f"Key {api_key}"},
            timeout=timeout,
            verify=verify_ssl,
        )

    async def close(self) -> None:
        """Close the HTTP client."""
        await self._client.aclose()

    async def execute(self, query_id: int) -> dict[str, Any]:
        """Get query details by ID.

        Args:
            query_id: Query ID

        Returns:
            Query details including SQL, name, and metadata
        """
        response = await self._client.get(f"/api/queries/{query_id}")
        response.raise_for_status()
        return response.json()
