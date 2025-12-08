"""MCP tool for list_dashboards."""

import json
from typing import Any

from mcp.types import TextContent, Tool


def get_tool() -> Tool:
    """Get list_dashboards tool definition."""
    return Tool(
        name="list_dashboards",
        description="List all dashboards in Redash.",
        inputSchema={
            "type": "object",
            "properties": {
                "page": {
                    "type": "integer",
                    "description": "Page number (default: 1)",
                },
                "page_size": {
                    "type": "integer",
                    "description": "Number of results per page (default: 25)",
                },
            },
            "required": [],
        },
    )


async def handle(client: Any, arguments: dict[str, Any]) -> list[TextContent]:
    """Handle list_dashboards tool call."""
    try:
        page = arguments.get("page", 1)
        page_size = arguments.get("page_size", 25)
        result = await client.execute(page=page, page_size=page_size)
        return [TextContent(type="text", text=json.dumps(result, indent=2, ensure_ascii=False))]

    except Exception as e:
        return [TextContent(type="text", text=f"Error: {e!s}")]
