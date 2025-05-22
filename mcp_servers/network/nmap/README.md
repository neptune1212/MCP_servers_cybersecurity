# Nmap MCP Server

This module provides advanced network scanning capabilities via the MCP protocol, using [Nmap](https://nmap.org/).

## Features

- `nmap_scan_top_ports`: Scan the top ports of a target
- `nmap_dns_brute_force`: Discover subdomains via DNS brute force
- `nmap_list_scan`: List scan for host discovery
- `nmap_os_detection`: Detect operating system
- `nmap_version_detection`: Detect service versions
- `nmap_syn_scan`: SYN scan for stealth port scanning
- `nmap_tcp_scan`: TCP connect scan
- `nmap_udp_scan`: UDP scan
- `nmap_fin_scan`: FIN scan for firewall evasion
- `nmap_idle_scan`: Idle scan for stealth
- `nmap_ping_scan`: Ping scan for host discovery
- `nmap_portscan_only`: Port scan only
- `nmap_no_portscan`: Host discovery without port scan
- `nmap_arp_discovery`: ARP discovery on local networks
- `nmap_disable_dns_resolution`: Scan with DNS resolution disabled

## Usage

### Prerequisites
- Python 3.8+
- [Nmap](https://nmap.org/) installed and available in your PATH
- [python-nmap](https://pypi.org/project/python-nmap/) Python package installed
- [fastmcp](https://github.com/modelcontext/fastmcp) Python package installed

### Running the Server

```sh
python nmap_mcp_server.py --host 0.0.0.0 --port 8000 --debug
```

- `--host`: Host for the MCP SSE server (default: localhost)
- `--port`: Port for the MCP SSE server (default: 8000)
- `--debug`: Enable debug logging

### Example Tool Usage

Each tool is exposed via the MCP protocol. Example tool calls:

- **Scan Top Ports:**
  - `nmap_scan_top_ports(target="192.168.1.1")`
- **DNS Brute Force:**
  - `nmap_dns_brute_force(target="example.com")`
- **OS Detection:**
  - `nmap_os_detection(target="192.168.1.1")`
- **Version Detection:**
  - `nmap_version_detection(target="192.168.1.1")`
- **SYN Scan:**
  - `nmap_syn_scan(target="192.168.1.1")`
- **TCP Scan:**
  - `nmap_tcp_scan(target="192.168.1.1")`
- **UDP Scan:**
  - `nmap_udp_scan(target="192.168.1.1")`
- **ARP Discovery:**
  - `nmap_arp_discovery(target="192.168.1.0/24")`

You can also pass additional Nmap arguments using the `args` parameter for advanced usage.

## Security Notice

**Use Nmap and this server only on systems you own or have explicit permission to test. Unauthorized scanning is illegal.**

See the main project [README](../../../README.md) for overall setup and integration details.