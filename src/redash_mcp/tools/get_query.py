"""MCP tool for get_query."""

import json
from typing import Any

from mcp.types import TextContent, Tool


def get_tool() -> Tool:
    """Get get_query tool definition."""
    return Tool(
        name="get_query",
        description="Get details of a specific query by ID.",
        inputSchema={
            "type": "object",
            "properties": {
                "query_id": {
                    "type": "integer",
                    "description": "The ID of the query to retrieve",
                },
            },
            "required": ["query_id"],
        },
    )


async def handle(client: Any, arguments: dict[str, Any]) -> list[TextContent]:
    """Handle get_query tool call.

    Args:
        client: API client instance
        arguments: Tool arguments

    Returns:
        List of TextContent with results
    """
    try:
        query_id = arguments.get("query_id")
        if query_id is None:
            return [TextContent(type="text", text="Error: query_id is required")]

        result = await client.execute(query_id=query_id)
        return [TextContent(type="text", text=json.dumps(result, indent=2, ensure_ascii=False))]

    except Exception as e:
        return [TextContent(type="text", text=f"Error: {str(e)}")]
