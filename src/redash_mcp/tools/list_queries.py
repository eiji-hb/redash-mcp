"""MCP tool for list_queries."""

import json
from typing import Any

from mcp.types import TextContent, Tool


def get_tool() -> Tool:
    """Get list_queries tool definition."""
    return Tool(
        name="list_queries",
        description="List all saved SQL queries in Redash. Returns query name, ID, and metadata.",
        inputSchema={
            "type": "object",
            "properties": {
                "page": {
                    "type": "integer",
                    "description": "Page number (default: 1)",
                    "default": 1,
                },
                "page_size": {
                    "type": "integer",
                    "description": "Number of results per page (default: 25, max: 100)",
                    "default": 25,
                },
            },
        },
    )


async def handle(client: Any, arguments: dict[str, Any]) -> list[TextContent]:
    """Handle list_queries tool call.

    Args:
        client: API client instance
        arguments: Tool arguments

    Returns:
        List of TextContent with results
    """
    try:
        result = await client.execute(
            page=arguments.get("page", 1),
            page_size=arguments.get("page_size", 25),
        )
        return [TextContent(type="text", text=json.dumps(result, indent=2, ensure_ascii=False))]

    except Exception as e:
        return [TextContent(type="text", text=f"Error: {str(e)}")]
