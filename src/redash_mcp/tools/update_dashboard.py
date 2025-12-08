"""MCP tool for update_dashboard."""

import json
from typing import Any

from mcp.types import TextContent, Tool


def get_tool() -> Tool:
    """Get update_dashboard tool definition."""
    return Tool(
        name="update_dashboard",
        description="Update an existing dashboard in Redash.",
        inputSchema={
            "type": "object",
            "properties": {
                "dashboard_id": {
                    "type": "integer",
                    "description": "ID of the dashboard to update",
                },
                "name": {
                    "type": "string",
                    "description": "New name for the dashboard",
                },
            },
            "required": ["dashboard_id"],
        },
    )


async def handle(client: Any, arguments: dict[str, Any]) -> list[TextContent]:
    """Handle update_dashboard tool call."""
    try:
        dashboard_id = arguments.get("dashboard_id")
        if dashboard_id is None:
            return [TextContent(type="text", text="Error: dashboard_id is required")]

        name = arguments.get("name")
        result = await client.execute(dashboard_id=dashboard_id, name=name)
        return [TextContent(type="text", text=json.dumps(result, indent=2, ensure_ascii=False))]

    except Exception as e:
        return [TextContent(type="text", text=f"Error: {e!s}")]
