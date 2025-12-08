"""MCP tool for update_data_source."""

import json
from typing import Any

from mcp.types import TextContent, Tool


def get_tool() -> Tool:
    """Get update_data_source tool definition."""
    return Tool(
        name="update_data_source",
        description="Update an existing data source in Redash.",
        inputSchema={
            "type": "object",
            "properties": {
                "data_source_id": {
                    "type": "integer",
                    "description": "ID of the data source to update",
                },
                "name": {
                    "type": "string",
                    "description": "New name for the data source",
                },
                "options": {
                    "type": "object",
                    "description": "New connection options for the data source",
                },
            },
            "required": ["data_source_id"],
        },
    )


async def handle(client: Any, arguments: dict[str, Any]) -> list[TextContent]:
    """Handle update_data_source tool call."""
    try:
        data_source_id = arguments.get("data_source_id")
        if data_source_id is None:
            return [TextContent(type="text", text="Error: data_source_id is required")]

        name = arguments.get("name")
        options = arguments.get("options")
        result = await client.execute(data_source_id=data_source_id, name=name, options=options)
        return [TextContent(type="text", text=json.dumps(result, indent=2, ensure_ascii=False))]

    except Exception as e:
        return [TextContent(type="text", text=f"Error: {e!s}")]
