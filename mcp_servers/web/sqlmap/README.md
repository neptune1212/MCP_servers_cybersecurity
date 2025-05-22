# Sqlmap MCP Server

This module provides SQL injection testing capabilities via the MCP protocol, using [sqlmap](https://sqlmap.org/).

## Features

- `sqlmap_basic_scan`: Basic SQL injection scan
- `sqlmap_get_databases`: Enumerate databases
- `sqlmap_get_tables`: Enumerate tables in a database
- `sqlmap_get_columns`: Enumerate columns in a table
- `sqlmap_dump_data`: Dump data from a table

## Usage

### Prerequisites
- Python 3.8+
- [sqlmap](https://sqlmap.org/) installed and available in your PATH
- [fastmcp](https://github.com/modelcontext/fastmcp) Python package installed

### Running the Server

```sh
python sqlmap_mcp_server.py --host 0.0.0.0 --port 8000 --debug
```

- `--host`: Host for the MCP SSE server (default: localhost)
- `--port`: Port for the MCP SSE server (default: 8000)
- `--debug`: Enable debug logging

### Example Tool Usage

Each tool is exposed via the MCP protocol. Example tool calls:

- **Basic Scan:**
  - `sqlmap_basic_scan(target="http://example.com/vuln.php?id=1")`
- **Get Databases:**
  - `sqlmap_get_databases(target="http://example.com/vuln.php?id=1")`
- **Get Tables:**
  - `sqlmap_get_tables(target="http://example.com/vuln.php?id=1", database="testdb")`
- **Get Columns:**
  - `sqlmap_get_columns(target="http://example.com/vuln.php?id=1", database="testdb", table="users")`
- **Dump Data:**
  - `sqlmap_dump_data(target="http://example.com/vuln.php?id=1", database="testdb", table="users")`

You can also pass additional sqlmap arguments using the `args` parameter for advanced usage.

## Security Notice

**Use sqlmap and this server only on systems you own or have explicit permission to test. Unauthorized testing is illegal.**

See the main project [README](../../../README.md) for overall setup and integration details.