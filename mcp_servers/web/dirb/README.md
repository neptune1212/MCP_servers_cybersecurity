# Dirb MCP Server

This module provides web content scanning via the MCP protocol, using [Dirb](http://dirb.sourceforge.net/).

## Features

- `dirb_basic_scan`: Basic directory scan
- `dirb_recursive_scan`: Recursive scan
- `dirb_custom_wordlist_scan`: Scan with custom wordlist and extensions

## Usage

### Prerequisites
- Python 3.8+
- [Dirb](http://dirb.sourceforge.net/) installed and available in your PATH
- [fastmcp](https://github.com/modelcontext/fastmcp) Python package installed

### Running the Server

```sh
python dirb_mcp_server.py --host 0.0.0.0 --port 8088 --debug
```

- `--host`: Host for the MCP SSE server (default: localhost)
- `--port`: Port for the MCP SSE server (default: 8088)
- `--debug`: Enable debug logging

### Example Tool Usage

- **Basic Scan:**
  - `dirb_basic_scan(url="http://example.com")`
- **Recursive Scan:**
  - `dirb_recursive_scan(url="http://example.com")`
- **Custom Wordlist Scan:**
  - `dirb_custom_wordlist_scan(url="http://example.com", wordlist="/path/to/wordlist.txt", extensions="php,html")`

You can also pass additional Dirb arguments using the `args` parameter for advanced usage.

## Security Notice

**Use Dirb and this server only on systems you own or have explicit permission to test. Unauthorized testing is illegal.**

See the main project [README](../../../README.md) for overall setup and integration details.
