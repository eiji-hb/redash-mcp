"""MCP tool for update_query."""

import json
from typing import Any

from mcp.types import TextContent, Tool


def get_tool() -> Tool:
    """Get update_query tool definition."""
    return Tool(
        name="update_query",
        description="Update an existing SQL query in Redash.",
        inputSchema={
            "type": "object",
            "properties": {
                "query_id": {
                    "type": "integer",
                    "description": "ID of the query to update",
                },
                "name": {
                    "type": "string",
                    "description": "New query name",
                },
                "query": {
                    "type": "string",
                    "description": "New SQL query string",
                },
                "data_source_id": {
                    "type": "integer",
                    "description": "New data source ID",
                },
                "description": {
                    "type": "string",
                    "description": "New description",
                },
            },
            "required": ["query_id"],
        },
    )


async def handle(client: Any, arguments: dict[str, Any]) -> list[TextContent]:
    """Handle update_query tool call."""
    try:
        query_id = arguments.get("query_id")
        if query_id is None:
            return [TextContent(type="text", text="Error: query_id is required")]

        result = await client.execute(
            query_id=query_id,
            name=arguments.get("name"),
            query=arguments.get("query"),
            data_source_id=arguments.get("data_source_id"),
            description=arguments.get("description"),
        )
        return [TextContent(type="text", text=json.dumps(result, indent=2, ensure_ascii=False))]

    except Exception as e:
        return [TextContent(type="text", text=f"Error: {e!s}")]
