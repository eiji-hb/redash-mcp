"""MCP tool definitions."""

from typing import Any

from mcp.types import TextContent, Tool

from .list_queries import get_tool as list_queries_tool
from .list_queries import handle as list_queries_handle

# ツール名とハンドラのマッピング
TOOL_HANDLERS = {
    "list_queries": list_queries_handle,
    # 追加時: "get_query": get_query_handle,
}


def get_all_tools() -> list[Tool]:
    """Get all available MCP tools."""
    return [
        list_queries_tool(),
        # 追加時: get_query_tool(),
    ]


async def handle_tool(client: Any, name: str, arguments: dict[str, Any]) -> list[TextContent]:
    """Route tool calls to appropriate handler."""
    handler = TOOL_HANDLERS.get(name)
    if handler:
        return await handler(client, arguments)
    return [TextContent(type="text", text=f"Unknown tool: {name}")]
