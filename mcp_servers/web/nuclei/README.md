# Nuclei MCP Server

This module provides fast vulnerability scanning via the MCP protocol, using [Nuclei](https://github.com/projectdiscovery/nuclei).

## Features

- `nuclei_basic_scan`: Basic scan with templates
- `nuclei_severity_scan`: Scan with severity filtering
- `nuclei_headless_scan`: Headless mode scan with custom headers

## Usage

### Prerequisites
- Python 3.8+
- [Nuclei](https://github.com/projectdiscovery/nuclei) installed and available in your PATH
- [fastmcp](https://github.com/modelcontext/fastmcp) Python package installed

### Running the Server

```sh
python nuclei_mcp_server.py --host 0.0.0.0 --port 8088 --debug
```

- `--host`: Host for the MCP SSE server (default: localhost)
- `--port`: Port for the MCP SSE server (default: 8088)
- `--debug`: Enable debug logging

### Example Tool Usage

- **Basic Scan:**
  - `nuclei_basic_scan(target="http://example.com", template="cves/2021/CVE-2021-1234.yaml")`
- **Severity Scan:**
  - `nuclei_severity_scan(target="http://example.com", severity="critical,high")`
- **Headless Scan:**
  - `nuclei_headless_scan(target="http://example.com", headers="User-Agent: Custom", headless=True)`

You can also pass additional Nuclei arguments using the `args` parameter for advanced usage.

## Security Notice

**Use Nuclei and this server only on systems you own or have explicit permission to test. Unauthorized testing is illegal.**

See the main project [README](../../../README.md) for overall setup and integration details.
