"""MCP tool definitions."""

from typing import Any

from mcp.types import TextContent, Tool

from .archive_dashboard import get_tool as archive_dashboard_tool
from .archive_dashboard import handle as archive_dashboard_handle
from .archive_query import get_tool as archive_query_tool
from .archive_query import handle as archive_query_handle
from .create_dashboard import get_tool as create_dashboard_tool
from .create_dashboard import handle as create_dashboard_handle
from .create_query import get_tool as create_query_tool
from .create_query import handle as create_query_handle
from .execute_query import get_tool as execute_query_tool
from .execute_query import handle as execute_query_handle
from .get_dashboard import get_tool as get_dashboard_tool
from .get_dashboard import handle as get_dashboard_handle
from .get_job import get_tool as get_job_tool
from .get_job import handle as get_job_handle
from .get_query import get_tool as get_query_tool
from .get_query import handle as get_query_handle
from .get_query_result import get_tool as get_query_result_tool
from .get_query_result import handle as get_query_result_handle
from .get_query_result_by_id import get_tool as get_query_result_by_id_tool
from .get_query_result_by_id import handle as get_query_result_by_id_handle
from .list_dashboards import get_tool as list_dashboards_tool
from .list_dashboards import handle as list_dashboards_handle
from .list_queries import get_tool as list_queries_tool
from .list_queries import handle as list_queries_handle
from .update_dashboard import get_tool as update_dashboard_tool
from .update_dashboard import handle as update_dashboard_handle
from .update_query import get_tool as update_query_tool
from .update_query import handle as update_query_handle

TOOL_HANDLERS = {
    "list_queries": list_queries_handle,
    "get_query": get_query_handle,
    "create_query": create_query_handle,
    "update_query": update_query_handle,
    "archive_query": archive_query_handle,
    "get_query_result": get_query_result_handle,
    "execute_query": execute_query_handle,
    "get_query_result_by_id": get_query_result_by_id_handle,
    "get_job": get_job_handle,
    "list_dashboards": list_dashboards_handle,
    "get_dashboard": get_dashboard_handle,
    "create_dashboard": create_dashboard_handle,
    "update_dashboard": update_dashboard_handle,
    "archive_dashboard": archive_dashboard_handle,
}


def get_all_tools() -> list[Tool]:
    """Get all available MCP tools."""
    return [
        list_queries_tool(),
        get_query_tool(),
        create_query_tool(),
        update_query_tool(),
        archive_query_tool(),
        get_query_result_tool(),
        execute_query_tool(),
        get_query_result_by_id_tool(),
        get_job_tool(),
        list_dashboards_tool(),
        get_dashboard_tool(),
        create_dashboard_tool(),
        update_dashboard_tool(),
        archive_dashboard_tool(),
    ]


async def handle_tool(client: Any, name: str, arguments: dict[str, Any]) -> list[TextContent]:
    """Route tool calls to appropriate handler."""
    handler = TOOL_HANDLERS.get(name)
    if handler:
        return await handler(client, arguments)
    return [TextContent(type="text", text=f"Unknown tool: {name}")]
