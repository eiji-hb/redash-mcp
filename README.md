# redash-mcp

MCP (Model Context Protocol) server for Redash API integration.

[日本語版はこちら](README.ja.md)

## Requirements

- Python 3.10+
- [uv](https://docs.astral.sh/uv/)

## Installation

```bash
# Clone the repository
git clone https://github.com/eiji-hb/redash-mcp.git
cd redash-mcp

# Install dependencies
uv sync
```

## Configuration

Set the following environment variables:

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `REDASH_URL` | Yes | - | Redash instance URL |
| `REDASH_API_KEY` | Yes | - | Redash API key |
| `REDASH_TIMEOUT` | No | 30000 | Request timeout in milliseconds |

## Usage

### With Claude Desktop

Add to your Claude Desktop config (`~/Library/Application Support/Claude/claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "redash": {
      "command": "uv",
      "args": ["--directory", "/path/to/redash-mcp", "run", "redash-mcp"],
      "env": {
        "REDASH_URL": "https://your-redash-instance.example.com",
        "REDASH_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

> **Note**: Environment variables must be set in the `env` section of the config. The `.env` file is not loaded when running from Claude Desktop.

### Standalone

```bash
# Set environment variables
export REDASH_URL=https://your-redash-instance.example.com
export REDASH_API_KEY=your-api-key-here

# Or create a .env file
uv run redash-mcp
```

## Available Tools

### Queries
- `list_queries` - List all saved SQL queries in Redash
- `get_query` - Get details of a specific query by ID
- `create_query` - Create a new SQL query
- `update_query` - Update an existing query

## License

MIT
