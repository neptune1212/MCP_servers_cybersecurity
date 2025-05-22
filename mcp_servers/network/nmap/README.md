# Nmap MCP Server

This module exposes Nmap's advanced network scanning capabilities via the MCP protocol.

## Features

- nmap_scan_top_ports: Scan the top ports of a target
- nmap_dns_brute_force: Discover subdomains via DNS brute force
- nmap_list_scan: List scan for host discovery
- nmap_os_detection: Detect operating system
- nmap_version_detection: Detect service versions
- nmap_syn_scan: SYN scan for stealth port scanning
- nmap_tcp_scan: TCP connect scan
- nmap_udp_scan: UDP scan
- nmap_fin_scan: FIN scan for firewall evasion
- nmap_idle_scan: Idle scan for stealth
- nmap_ping_scan: Ping scan for host discovery
- nmap_portscan_only: Port scan only
- nmap_no_portscan: Host discovery without port scan
- nmap_arp_discovery: ARP discovery on local networks
- nmap_disable_dns_resolution: Scan with DNS resolution disabled

## Usage

This server is intended to be run as part of the MCP Servers Cybersecurity platform. It exposes Nmap's scanning features as callable MCP tools. Each function is prefixed with `nmap_` for clarity.

See the main project [README](../../../README.md) for setup, deployment, and integration details.