"""MCP tool for get_dashboard."""

import json
from typing import Any

from mcp.types import TextContent, Tool


def get_tool() -> Tool:
    """Get get_dashboard tool definition."""
    return Tool(
        name="get_dashboard",
        description="Get a dashboard by its slug.",
        inputSchema={
            "type": "object",
            "properties": {
                "dashboard_slug": {
                    "type": "string",
                    "description": "Slug of the dashboard to retrieve",
                },
            },
            "required": ["dashboard_slug"],
        },
    )


async def handle(client: Any, arguments: dict[str, Any]) -> list[TextContent]:
    """Handle get_dashboard tool call."""
    try:
        dashboard_slug = arguments.get("dashboard_slug")
        if dashboard_slug is None:
            return [TextContent(type="text", text="Error: dashboard_slug is required")]

        result = await client.execute(dashboard_slug=dashboard_slug)
        return [TextContent(type="text", text=json.dumps(result, indent=2, ensure_ascii=False))]

    except Exception as e:
        return [TextContent(type="text", text=f"Error: {e!s}")]
