"""Redash get_job API."""

from typing import Any

import httpx


class GetJobClient:
    """Client for get_job API."""

    def __init__(self, base_url: str, api_key: str, timeout: float = 30.0) -> None:
        self.base_url = base_url.rstrip("/")
        self._client = httpx.AsyncClient(
            base_url=self.base_url,
            headers={"Authorization": f"Key {api_key}"},
            timeout=timeout,
        )

    async def close(self) -> None:
        await self._client.aclose()

    async def execute(self, job_id: str) -> dict[str, Any]:
        """Get a job status.

        Args:
            job_id: ID of the job

        Returns:
            Job object with status and query_result_id (if success)

        Note:
            Status codes:
            1 = PENDING (waiting to be executed)
            2 = STARTED (executing)
            3 = SUCCESS
            4 = FAILURE
            5 = CANCELLED
        """
        response = await self._client.get(f"/api/jobs/{job_id}")
        response.raise_for_status()
        return response.json()
