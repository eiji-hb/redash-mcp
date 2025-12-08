"""MCP tool for get_query_result_by_id."""

import json
from typing import Any

from mcp.types import TextContent, Tool


def get_tool() -> Tool:
    """Get get_query_result_by_id tool definition."""
    return Tool(
        name="get_query_result_by_id",
        description="Get a query result by its result ID (not query ID).",
        inputSchema={
            "type": "object",
            "properties": {
                "query_result_id": {
                    "type": "integer",
                    "description": "ID of the query result to retrieve",
                },
            },
            "required": ["query_result_id"],
        },
    )


async def handle(client: Any, arguments: dict[str, Any]) -> list[TextContent]:
    """Handle get_query_result_by_id tool call."""
    try:
        query_result_id = arguments.get("query_result_id")
        if query_result_id is None:
            return [TextContent(type="text", text="Error: query_result_id is required")]

        result = await client.execute(query_result_id=query_result_id)
        return [TextContent(type="text", text=json.dumps(result, indent=2, ensure_ascii=False))]

    except Exception as e:
        return [TextContent(type="text", text=f"Error: {e!s}")]
