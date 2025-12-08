"""MCP tool for list_data_source_types."""

import json
from typing import Any

from mcp.types import TextContent, Tool


def get_tool() -> Tool:
    """Get list_data_source_types tool definition."""
    return Tool(
        name="list_data_source_types",
        description="List available data source types in Redash.",
        inputSchema={
            "type": "object",
            "properties": {},
            "required": [],
        },
    )


async def handle(client: Any, arguments: dict[str, Any]) -> list[TextContent]:
    """Handle list_data_source_types tool call."""
    try:
        result = await client.execute()
        return [TextContent(type="text", text=json.dumps(result, indent=2, ensure_ascii=False))]

    except Exception as e:
        return [TextContent(type="text", text=f"Error: {e!s}")]
