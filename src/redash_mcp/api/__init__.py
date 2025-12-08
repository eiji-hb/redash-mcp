"""Redash API clients."""

from typing import Any

from .create_query import CreateQueryClient
from .get_query import GetQueryClient
from .list_queries import ListQueriesClient

_clients: dict[str, Any] = {}


def get_client_for_tool(name: str, base_url: str, api_key: str, timeout: float) -> Any:
    """Get or create a client for the specified tool.

    Args:
        name: Tool name
        base_url: Redash instance URL
        api_key: Redash API key
        timeout: Request timeout in seconds

    Returns:
        API client instance for the tool
    """
    if name not in _clients:
        match name:
            case "list_queries":
                _clients[name] = ListQueriesClient(base_url, api_key, timeout)
            case "get_query":
                _clients[name] = GetQueryClient(base_url, api_key, timeout)
            case "create_query":
                _clients[name] = CreateQueryClient(base_url, api_key, timeout)
    return _clients.get(name)
