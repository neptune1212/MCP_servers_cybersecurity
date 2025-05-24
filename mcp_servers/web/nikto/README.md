# Nikto MCP Server

This module provides web vulnerability scanning via the MCP protocol, using [Nikto](https://cirt.net/Nikto2).

## Features

- `nikto_basic_scan`: Basic Nikto scan
- `nikto_ssl_scan`: SSL-specific scan
- `nikto_scan_with_plugins`: Scan with specific Nikto plugins

## Usage

### Prerequisites
- Python 3.8+
- [Nikto](https://cirt.net/Nikto2) installed and available in your PATH
- [fastmcp](https://github.com/modelcontext/fastmcp) Python package installed

### Running the Server

```sh
python nikto_mcp_server.py --host 0.0.0.0 --port 8088 --debug
```

- `--host`: Host for the MCP SSE server (default: localhost)
- `--port`: Port for the MCP SSE server (default: 8088)
- `--debug`: Enable debug logging

### Example Tool Usage

- **Basic Scan:**
  - `nikto_basic_scan(target="http://example.com")`
- **SSL Scan:**
  - `nikto_ssl_scan(target="https://example.com")`
- **Scan with Plugins:**
  - `nikto_scan_with_plugins(target="http://example.com", plugins="apache_expect_xss")`

You can also pass additional Nikto arguments using the `args` parameter for advanced usage.

## Security Notice

**Use Nikto and this server only on systems you own or have explicit permission to test. Unauthorized testing is illegal.**

See the main project [README](../../../README.md) for overall setup and integration details.
