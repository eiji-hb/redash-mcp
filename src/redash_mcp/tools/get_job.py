"""MCP tool for get_job."""

import json
from typing import Any

from mcp.types import TextContent, Tool


def get_tool() -> Tool:
    """Get get_job tool definition."""
    return Tool(
        name="get_job",
        description="Get job status. Status: 1=PENDING, 2=STARTED, 3=SUCCESS, 4=FAILURE, 5=CANCELLED.",
        inputSchema={
            "type": "object",
            "properties": {
                "job_id": {
                    "type": "string",
                    "description": "ID of the job to check",
                },
            },
            "required": ["job_id"],
        },
    )


async def handle(client: Any, arguments: dict[str, Any]) -> list[TextContent]:
    """Handle get_job tool call."""
    try:
        job_id = arguments.get("job_id")
        if job_id is None:
            return [TextContent(type="text", text="Error: job_id is required")]

        result = await client.execute(job_id=job_id)
        return [TextContent(type="text", text=json.dumps(result, indent=2, ensure_ascii=False))]

    except Exception as e:
        return [TextContent(type="text", text=f"Error: {e!s}")]
