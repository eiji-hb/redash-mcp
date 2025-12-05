"""Redash MCP Server implementation."""

import asyncio
from typing import Any

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import TextContent, Tool

from .api import ListQueriesClient
from .config import get_settings
from .tools import get_all_tools, handle_tool

server = Server("redash-mcp")
client: ListQueriesClient | None = None


def get_client() -> ListQueriesClient:
    """Get the client instance."""
    global client
    if client is None:
        settings = get_settings()
        client = ListQueriesClient(
            settings.url,
            settings.api_key,
            timeout=settings.timeout / 1000.0,
        )
    return client


@server.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools."""
    return get_all_tools()


@server.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> list[TextContent]:
    """Handle tool calls."""
    return await handle_tool(get_client(), name, arguments)


async def run_server() -> None:
    """Run the MCP server."""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


def main() -> None:
    """Main entry point."""
    asyncio.run(run_server())


if __name__ == "__main__":
    main()
