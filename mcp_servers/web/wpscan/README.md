# WPScan MCP Server

This module provides WordPress security scanning via the MCP protocol, using [WPScan](https://github.com/wpscanteam/wpscan).

## Features

- `wpscan_basic_scan`: Basic WordPress scan
- `wpscan_vuln_scan`: Scan with vulnerability detection using API token
- `wpscan_enumerate`: Enumerate users, plugins, and themes

## Usage

### Prerequisites
- Python 3.8+
- [WPScan](https://github.com/wpscanteam/wpscan) installed and available in your PATH
- [fastmcp](https://github.com/modelcontext/fastmcp) Python package installed

### Running the Server

```sh
python wpscan_mcp_server.py --host 0.0.0.0 --port 8088 --debug
```

- `--host`: Host for the MCP SSE server (default: localhost)
- `--port`: Port for the MCP SSE server (default: 8088)
- `--debug`: Enable debug logging

### Example Tool Usage

- **Basic Scan:**
  - `wpscan_basic_scan(target="http://example.com")`
- **Vulnerability Scan:**
  - `wpscan_vuln_scan(target="http://example.com", api_token="YOUR_API_TOKEN")`
- **Enumerate:**
  - `wpscan_enumerate(target="http://example.com", enum_type="u,ap,at")`

You can also pass additional WPScan arguments using the `args` parameter for advanced usage.

## Security Notice

**Use WPScan and this server only on systems you own or have explicit permission to test. Unauthorized testing is illegal.**

See the main project [README](../../../README.md) for overall setup and integration details.
