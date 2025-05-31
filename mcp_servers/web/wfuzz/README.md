# Wfuzz MCP Server

This module provides web application fuzzing via the MCP protocol, using [Wfuzz](https://github.com/xmendez/wfuzz).

## Features

- `wfuzz_basic_fuzz`: Basic fuzzing
- `wfuzz_multi_injection`: Fuzzing with multiple injection points
- `wfuzz_custom_headers`: Fuzzing with custom headers and authentication

## Usage

### Prerequisites
- Python 3.8+
- [Wfuzz](https://github.com/xmendez/wfuzz) installed and available in your PATH
- [fastmcp](https://github.com/modelcontext/fastmcp) Python package installed

### Running the Server

```sh
python wfuzz_mcp_server.py --host 0.0.0.0 --port 8088 --debug
```

- `--host`: Host for the MCP SSE server (default: localhost)
- `--port`: Port for the MCP SSE server (default: 8088)
- `--debug`: Enable debug logging

### Example Tool Usage

- **Basic Fuzz:**
  - `wfuzz_basic_fuzz(url="http://example.com/FUZZ", wordlist="/path/to/wordlist.txt")`
- **Multi Injection:**
  - `wfuzz_multi_injection(url="http://example.com/FUZZ/FUZZ", wordlists=["/path/1.txt","/path/2.txt"])`
- **Custom Headers:**
  - `wfuzz_custom_headers(url="http://example.com/FUZZ", wordlist="/path/to/wordlist.txt", headers="Authorization: Basic ...")`

You can also pass additional Wfuzz arguments using the `args` parameter for advanced usage.

## Security Notice

**Use Wfuzz and this server only on systems you own or have explicit permission to test. Unauthorized testing is illegal.**

See the main project [README](../../../README.md) for overall setup and integration details.
