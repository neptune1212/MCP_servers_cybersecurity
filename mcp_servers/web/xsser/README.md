# XSSer MCP Server

This module provides XSS vulnerability detection and exploitation via the MCP protocol, using [XSSer](https://github.com/epsylon/xsser).

## Features

- `xsser_basic_scan`: Basic XSS scan
- `xsser_payload_scan`: Scan with specific payloads
- `xsser_auto_scan`: Auto-inject vectors and use bypass techniques

## Usage

### Prerequisites
- Python 3.8+
- [XSSer](https://github.com/epsylon/xsser) installed and available in your PATH
- [fastmcp](https://github.com/modelcontext/fastmcp) Python package installed

### Running the Server

```sh
python xsser_mcp_server.py --host 0.0.0.0 --port 8088 --debug
```

- `--host`: Host for the MCP SSE server (default: localhost)
- `--port`: Port for the MCP SSE server (default: 8088)
- `--debug`: Enable debug logging

### Example Tool Usage

- **Basic Scan:**
  - `xsser_basic_scan(url="http://example.com/vuln.php?q=FUZZ")`
- **Payload Scan:**
  - `xsser_payload_scan(url="http://example.com/vuln.php?q=FUZZ", payload="<script>alert(1)</script>")`
- **Auto Scan:**
  - `xsser_auto_scan(url="http://example.com/vuln.php?q=FUZZ")`

You can also pass additional XSSer arguments using the `args` parameter for advanced usage.

## Security Notice

**Use XSSer and this server only on systems you own or have explicit permission to test. Unauthorized testing is illegal.**

See the main project [README](../../../README.md) for overall setup and integration details.
