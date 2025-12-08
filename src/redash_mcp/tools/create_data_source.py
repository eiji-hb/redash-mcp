"""MCP tool for create_data_source."""

import json
from typing import Any

from mcp.types import TextContent, Tool


def get_tool() -> Tool:
    """Get create_data_source tool definition."""
    return Tool(
        name="create_data_source",
        description="Create a new data source in Redash.",
        inputSchema={
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "Name of the data source",
                },
                "type": {
                    "type": "string",
                    "description": "Type of the data source (e.g., 'pg', 'mysql', 'bigquery')",
                },
                "options": {
                    "type": "object",
                    "description": "Connection options for the data source",
                },
            },
            "required": ["name", "type", "options"],
        },
    )


async def handle(client: Any, arguments: dict[str, Any]) -> list[TextContent]:
    """Handle create_data_source tool call."""
    try:
        name = arguments.get("name")
        type_ = arguments.get("type")
        options = arguments.get("options")

        if name is None:
            return [TextContent(type="text", text="Error: name is required")]
        if type_ is None:
            return [TextContent(type="text", text="Error: type is required")]
        if options is None:
            return [TextContent(type="text", text="Error: options is required")]

        result = await client.execute(name=name, type=type_, options=options)
        return [TextContent(type="text", text=json.dumps(result, indent=2, ensure_ascii=False))]

    except Exception as e:
        return [TextContent(type="text", text=f"Error: {e!s}")]
