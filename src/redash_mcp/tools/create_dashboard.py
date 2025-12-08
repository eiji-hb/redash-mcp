"""MCP tool for create_dashboard."""

import json
from typing import Any

from mcp.types import TextContent, Tool


def get_tool() -> Tool:
    """Get create_dashboard tool definition."""
    return Tool(
        name="create_dashboard",
        description="Create a new dashboard in Redash.",
        inputSchema={
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "Name of the dashboard",
                },
            },
            "required": ["name"],
        },
    )


async def handle(client: Any, arguments: dict[str, Any]) -> list[TextContent]:
    """Handle create_dashboard tool call."""
    try:
        name = arguments.get("name")
        if name is None:
            return [TextContent(type="text", text="Error: name is required")]

        result = await client.execute(name=name)
        return [TextContent(type="text", text=json.dumps(result, indent=2, ensure_ascii=False))]

    except Exception as e:
        return [TextContent(type="text", text=f"Error: {e!s}")]
