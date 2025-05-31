# Gobuster MCP Server

This module provides directory, DNS, and vhost brute-forcing via the MCP protocol, using [Gobuster](https://github.com/OJ/gobuster).

## Features

- `gobuster_dir_scan`: Directory brute-forcing
- `gobuster_dns_scan`: DNS subdomain enumeration
- `gobuster_vhost_scan`: Virtual host brute-forcing

## Usage

### Prerequisites
- Python 3.8+
- [Gobuster](https://github.com/OJ/gobuster) installed and available in your PATH
- [fastmcp](https://github.com/modelcontext/fastmcp) Python package installed

### Running the Server

```sh
python gobuster_mcp_server.py --host 0.0.0.0 --port 8088 --debug
```

- `--host`: Host for the MCP SSE server (default: localhost)
- `--port`: Port for the MCP SSE server (default: 8088)
- `--debug`: Enable debug logging

### Example Tool Usage

- **Directory Scan:**
  - `gobuster_dir_scan(url="http://example.com", wordlist="/path/to/wordlist.txt")`
- **DNS Scan:**
  - `gobuster_dns_scan(domain="example.com", wordlist="/path/to/wordlist.txt")`
- **Vhost Scan:**
  - `gobuster_vhost_scan(domain="example.com", wordlist="/path/to/wordlist.txt")`

You can also pass additional Gobuster arguments using the `args` parameter for advanced usage.

## Security Notice

**Use Gobuster and this server only on systems you own or have explicit permission to test. Unauthorized testing is illegal.**

See the main project [README](../../../README.md) for overall setup and integration details.
