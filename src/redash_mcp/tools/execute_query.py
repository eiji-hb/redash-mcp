"""MCP tool for execute_query."""

import json
from typing import Any

from mcp.types import TextContent, Tool


def get_tool() -> Tool:
    """Get execute_query tool definition."""
    return Tool(
        name="execute_query",
        description="Execute a query or get cached result. Supports parameterized queries.",
        inputSchema={
            "type": "object",
            "properties": {
                "query_id": {
                    "type": "integer",
                    "description": "ID of the query to execute",
                },
                "parameters": {
                    "type": "object",
                    "description": "Query parameters (for parameterized queries)",
                },
                "max_age": {
                    "type": "integer",
                    "description": "Max cache age in seconds. Set to 0 to force fresh execution.",
                },
            },
            "required": ["query_id"],
        },
    )


async def handle(client: Any, arguments: dict[str, Any]) -> list[TextContent]:
    """Handle execute_query tool call."""
    try:
        query_id = arguments.get("query_id")
        if query_id is None:
            return [TextContent(type="text", text="Error: query_id is required")]

        result = await client.execute(
            query_id=query_id,
            parameters=arguments.get("parameters"),
            max_age=arguments.get("max_age"),
        )
        return [TextContent(type="text", text=json.dumps(result, indent=2, ensure_ascii=False))]

    except Exception as e:
        return [TextContent(type="text", text=f"Error: {e!s}")]
