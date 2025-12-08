"""Redash API clients."""

from typing import Any

from .archive_dashboard import ArchiveDashboardClient
from .archive_query import ArchiveQueryClient
from .create_dashboard import CreateDashboardClient
from .create_data_source import CreateDataSourceClient
from .create_query import CreateQueryClient
from .delete_data_source import DeleteDataSourceClient
from .execute_query import ExecuteQueryClient
from .get_dashboard import GetDashboardClient
from .get_data_source import GetDataSourceClient
from .get_data_source_schema import GetDataSourceSchemaClient
from .get_job import GetJobClient
from .get_query import GetQueryClient
from .get_query_result import GetQueryResultClient
from .get_query_result_by_id import GetQueryResultByIdClient
from .list_dashboards import ListDashboardsClient
from .list_data_source_types import ListDataSourceTypesClient
from .list_data_sources import ListDataSourcesClient
from .list_queries import ListQueriesClient
from .test_data_source import TestDataSourceClient
from .update_dashboard import UpdateDashboardClient
from .update_data_source import UpdateDataSourceClient
from .update_query import UpdateQueryClient

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
            case "update_query":
                _clients[name] = UpdateQueryClient(base_url, api_key, timeout)
            case "archive_query":
                _clients[name] = ArchiveQueryClient(base_url, api_key, timeout)
            case "get_query_result":
                _clients[name] = GetQueryResultClient(base_url, api_key, timeout)
            case "execute_query":
                _clients[name] = ExecuteQueryClient(base_url, api_key, timeout)
            case "get_query_result_by_id":
                _clients[name] = GetQueryResultByIdClient(base_url, api_key, timeout)
            case "get_job":
                _clients[name] = GetJobClient(base_url, api_key, timeout)
            case "list_dashboards":
                _clients[name] = ListDashboardsClient(base_url, api_key, timeout)
            case "get_dashboard":
                _clients[name] = GetDashboardClient(base_url, api_key, timeout)
            case "create_dashboard":
                _clients[name] = CreateDashboardClient(base_url, api_key, timeout)
            case "update_dashboard":
                _clients[name] = UpdateDashboardClient(base_url, api_key, timeout)
            case "archive_dashboard":
                _clients[name] = ArchiveDashboardClient(base_url, api_key, timeout)
            case "list_data_sources":
                _clients[name] = ListDataSourcesClient(base_url, api_key, timeout)
            case "get_data_source":
                _clients[name] = GetDataSourceClient(base_url, api_key, timeout)
            case "create_data_source":
                _clients[name] = CreateDataSourceClient(base_url, api_key, timeout)
            case "update_data_source":
                _clients[name] = UpdateDataSourceClient(base_url, api_key, timeout)
            case "delete_data_source":
                _clients[name] = DeleteDataSourceClient(base_url, api_key, timeout)
            case "get_data_source_schema":
                _clients[name] = GetDataSourceSchemaClient(base_url, api_key, timeout)
            case "test_data_source":
                _clients[name] = TestDataSourceClient(base_url, api_key, timeout)
            case "list_data_source_types":
                _clients[name] = ListDataSourceTypesClient(base_url, api_key, timeout)
    return _clients.get(name)
