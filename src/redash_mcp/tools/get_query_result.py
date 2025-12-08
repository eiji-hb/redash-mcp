"""MCP tool for get_query_result."""

import json
from typing import Any

from mcp.types import TextContent, Tool


def get_tool() -> Tool:
    """Get get_query_result tool definition."""
    return Tool(
        name="get_query_result",
        description="Get cached result for a query. Only works for non-parameterized queries.",
        inputSchema={
            "type": "object",
            "properties": {
                "query_id": {
                    "type": "integer",
                    "description": "ID of the query to get results for",
                },
            },
            "required": ["query_id"],
        },
    )


async def handle(client: Any, arguments: dict[str, Any]) -> list[TextContent]:
    """Handle get_query_result tool call."""
    try:
        query_id = arguments.get("query_id")
        if query_id is None:
            return [TextContent(type="text", text="Error: query_id is required")]

        result = await client.execute(query_id=query_id)
        return [TextContent(type="text", text=json.dumps(result, indent=2, ensure_ascii=False))]

    except Exception as e:
        return [TextContent(type="text", text=f"Error: {e!s}")]
