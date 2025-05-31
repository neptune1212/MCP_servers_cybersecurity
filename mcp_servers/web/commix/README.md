# Commix MCP Server

This module provides command injection exploitation via the MCP protocol, using [Commix](https://github.com/commixproject/commix).

## Features

- `commix_basic_scan`: Basic command injection scan
- `commix_technique_scan`: Scan with specific techniques
- `commix_os_shell`: Automated exploitation with OS shell

## Usage

### Prerequisites
- Python 3.8+
- [Commix](https://github.com/commixproject/commix) installed and available in your PATH
- [fastmcp](https://github.com/modelcontext/fastmcp) Python package installed

### Running the Server

```sh
python commix_mcp_server.py --host 0.0.0.0 --port 8088 --debug
```

- `--host`: Host for the MCP SSE server (default: localhost)
- `--port`: Port for the MCP SSE server (default: 8088)
- `--debug`: Enable debug logging

### Example Tool Usage

- **Basic Scan:**
  - `commix_basic_scan(url="http://example.com/vuln.php?id=1")`
- **Technique Scan:**
  - `commix_technique_scan(url="http://example.com/vuln.php?id=1", technique="BEQ")`
- **OS Shell:**
  - `commix_os_shell(url="http://example.com/vuln.php?id=1")`

You can also pass additional Commix arguments using the `args` parameter for advanced usage.

## Security Notice

**Use Commix and this server only on systems you own or have explicit permission to test. Unauthorized testing is illegal.**

See the main project [README](../../../README.md) for overall setup and integration details.
