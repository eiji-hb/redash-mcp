"""MCP tool for get_data_source_schema."""

import json
from typing import Any

from mcp.types import TextContent, Tool


def get_tool() -> Tool:
    """Get get_data_source_schema tool definition."""
    return Tool(
        name="get_data_source_schema",
        description="Get schema (tables and columns) for a data source.",
        inputSchema={
            "type": "object",
            "properties": {
                "data_source_id": {
                    "type": "integer",
                    "description": "ID of the data source",
                },
                "refresh": {
                    "type": "boolean",
                    "description": "Force refresh the schema cache (default: false)",
                },
            },
            "required": ["data_source_id"],
        },
    )


async def handle(client: Any, arguments: dict[str, Any]) -> list[TextContent]:
    """Handle get_data_source_schema tool call."""
    try:
        data_source_id = arguments.get("data_source_id")
        if data_source_id is None:
            return [TextContent(type="text", text="Error: data_source_id is required")]

        refresh = arguments.get("refresh", False)
        result = await client.execute(data_source_id=data_source_id, refresh=refresh)
        return [TextContent(type="text", text=json.dumps(result, indent=2, ensure_ascii=False))]

    except Exception as e:
        return [TextContent(type="text", text=f"Error: {e!s}")]
