"""Redash MCP Server implementation."""

import asyncio
from typing import Any

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import TextContent, Tool

from .api import get_client_for_tool
from .config import get_settings
from .tools import get_all_tools, handle_tool

server = Server("redash-mcp")
_settings = None


def get_settings_cached():
    """Get cached settings."""
    global _settings
    if _settings is None:
        _settings = get_settings()
    return _settings


@server.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools."""
    return get_all_tools()


@server.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> list[TextContent]:
    """Handle tool calls."""
    settings = get_settings_cached()
    client = get_client_for_tool(
        name,
        settings.url,
        settings.api_key,
        settings.timeout / 1000.0,
    )
    if client is None:
        return [TextContent(type="text", text=f"Unknown tool: {name}")]
    return await handle_tool(client, name, arguments)


async def run_server() -> None:
    """Run the MCP server."""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


def main() -> None:
    """Main entry point."""
    asyncio.run(run_server())


if __name__ == "__main__":
    main()
