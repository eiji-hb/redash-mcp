"""MCP tool for create_query."""

import json
from typing import Any

from mcp.types import TextContent, Tool


def get_tool() -> Tool:
    """Get create_query tool definition."""
    return Tool(
        name="create_query",
        description="Create a new SQL query in Redash.",
        inputSchema={
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "Query name",
                },
                "query": {
                    "type": "string",
                    "description": "SQL query string",
                },
                "data_source_id": {
                    "type": "integer",
                    "description": "ID of the data source to run this query against",
                },
                "description": {
                    "type": "string",
                    "description": "Optional query description",
                },
            },
            "required": ["name", "query", "data_source_id"],
        },
    )


async def handle(client: Any, arguments: dict[str, Any]) -> list[TextContent]:
    """Handle create_query tool call."""
    try:
        name = arguments.get("name")
        query = arguments.get("query")
        data_source_id = arguments.get("data_source_id")

        if not name or not query or data_source_id is None:
            return [TextContent(type="text", text="Error: name, query, and data_source_id are required")]

        result = await client.execute(
            name=name,
            query=query,
            data_source_id=data_source_id,
            description=arguments.get("description"),
        )
        return [TextContent(type="text", text=json.dumps(result, indent=2, ensure_ascii=False))]

    except Exception as e:
        return [TextContent(type="text", text=f"Error: {e!s}")]
