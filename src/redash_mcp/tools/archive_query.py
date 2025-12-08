"""MCP tool for archive_query."""

import json
from typing import Any

from mcp.types import TextContent, Tool


def get_tool() -> Tool:
    """Get archive_query tool definition."""
    return Tool(
        name="archive_query",
        description="Archive (soft delete) a query in Redash.",
        inputSchema={
            "type": "object",
            "properties": {
                "query_id": {
                    "type": "integer",
                    "description": "ID of the query to archive",
                },
            },
            "required": ["query_id"],
        },
    )


async def handle(client: Any, arguments: dict[str, Any]) -> list[TextContent]:
    """Handle archive_query tool call."""
    try:
        query_id = arguments.get("query_id")
        if query_id is None:
            return [TextContent(type="text", text="Error: query_id is required")]

        result = await client.execute(query_id=query_id)
        return [TextContent(type="text", text=json.dumps(result, indent=2, ensure_ascii=False))]

    except Exception as e:
        return [TextContent(type="text", text=f"Error: {e!s}")]
