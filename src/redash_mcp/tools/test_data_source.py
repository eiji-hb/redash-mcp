"""MCP tool for test_data_source."""

import json
from typing import Any

from mcp.types import TextContent, Tool


def get_tool() -> Tool:
    """Get test_data_source tool definition."""
    return Tool(
        name="test_data_source",
        description="Test connection to a data source.",
        inputSchema={
            "type": "object",
            "properties": {
                "data_source_id": {
                    "type": "integer",
                    "description": "ID of the data source to test",
                },
            },
            "required": ["data_source_id"],
        },
    )


async def handle(client: Any, arguments: dict[str, Any]) -> list[TextContent]:
    """Handle test_data_source tool call."""
    try:
        data_source_id = arguments.get("data_source_id")
        if data_source_id is None:
            return [TextContent(type="text", text="Error: data_source_id is required")]

        result = await client.execute(data_source_id=data_source_id)
        return [TextContent(type="text", text=json.dumps(result, indent=2, ensure_ascii=False))]

    except Exception as e:
        return [TextContent(type="text", text=f"Error: {e!s}")]
