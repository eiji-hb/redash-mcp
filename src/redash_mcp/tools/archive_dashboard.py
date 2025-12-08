"""MCP tool for archive_dashboard."""

import json
from typing import Any

from mcp.types import TextContent, Tool


def get_tool() -> Tool:
    """Get archive_dashboard tool definition."""
    return Tool(
        name="archive_dashboard",
        description="Archive (soft delete) a dashboard in Redash.",
        inputSchema={
            "type": "object",
            "properties": {
                "dashboard_slug": {
                    "type": "string",
                    "description": "Slug of the dashboard to archive",
                },
            },
            "required": ["dashboard_slug"],
        },
    )


async def handle(client: Any, arguments: dict[str, Any]) -> list[TextContent]:
    """Handle archive_dashboard tool call."""
    try:
        dashboard_slug = arguments.get("dashboard_slug")
        if dashboard_slug is None:
            return [TextContent(type="text", text="Error: dashboard_slug is required")]

        result = await client.execute(dashboard_slug=dashboard_slug)
        return [TextContent(type="text", text=json.dumps(result, indent=2, ensure_ascii=False))]

    except Exception as e:
        return [TextContent(type="text", text=f"Error: {e!s}")]
