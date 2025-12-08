"""MCP tool definitions."""

from typing import Any

from mcp.types import TextContent, Tool

from .archive_query import get_tool as archive_query_tool
from .archive_query import handle as archive_query_handle
from .create_query import get_tool as create_query_tool
from .create_query import handle as create_query_handle
from .get_query import get_tool as get_query_tool
from .get_query import handle as get_query_handle
from .list_queries import get_tool as list_queries_tool
from .list_queries import handle as list_queries_handle
from .update_query import get_tool as update_query_tool
from .update_query import handle as update_query_handle

TOOL_HANDLERS = {
    "list_queries": list_queries_handle,
    "get_query": get_query_handle,
    "create_query": create_query_handle,
    "update_query": update_query_handle,
    "archive_query": archive_query_handle,
}


def get_all_tools() -> list[Tool]:
    """Get all available MCP tools."""
    return [
        list_queries_tool(),
        get_query_tool(),
        create_query_tool(),
        update_query_tool(),
        archive_query_tool(),
    ]


async def handle_tool(client: Any, name: str, arguments: dict[str, Any]) -> list[TextContent]:
    """Route tool calls to appropriate handler."""
    handler = TOOL_HANDLERS.get(name)
    if handler:
        return await handler(client, arguments)
    return [TextContent(type="text", text=f"Unknown tool: {name}")]
