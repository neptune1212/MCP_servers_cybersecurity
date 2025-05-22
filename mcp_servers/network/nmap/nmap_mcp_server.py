import argparse
import nmap
from fastmcp import FastMCP
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('Nmap-MCP-Server')

# Global debug flag
debug = False

# Initialize the MCP server with a name
mcp = FastMCP("Nmap MCP Server")
nm = nmap.PortScanner()

def execute_scan(target: str, args: str = "") -> dict:
    """
    Execute an Nmap scan using the specified arguments.

    Args:
        target (str): The target IP address or hostname.
        args (str): Additional Nmap command-line arguments.

    Returns:
        dict: The scan results.
    """
    if debug:
        logger.debug(f"Executing scan on target: {target} with arguments: {args}")
    return nm.scan(hosts=target, arguments=args)

@mcp.tool()
def nmap_scan_top_ports(target: str, args: str = "") -> dict:
    """
    Scan the top ports of the specified target with optional custom arguments.

    Args:
        target (str): The target hostname or IP address.
        args (str): Additional Nmap command-line arguments.

    Returns:
        dict: The scan results in JSON format.
    """
    if debug:
        logger.debug(f"Tool: nmap_scan_top_ports, Command: nmap {target} {args}")
    return execute_scan(target, args)

@mcp.tool()
def nmap_dns_brute_force(target: str, args: str = "") -> dict:
    """
    Perform DNS brute-force to discover subdomains of the specified target.

    Args:
        target (str): The target domain to scan.
        args (str): Additional Nmap command-line arguments.

    Returns:
        dict: The DNS brute-force scan results.
    """
    if debug:
        logger.debug(f"Tool: nmap_dns_brute_force, Command: nmap {target} --script dns-brute {args}")
    return execute_scan(target, f"--script dns-brute {args}")

@mcp.tool()
def nmap_list_scan(target: str, args: str = "") -> dict:
    """
    Perform a list scan on the specified target with optional custom arguments.

    Args:
        target (str): The target IP address or hostname.
        args (str): Additional Nmap command-line arguments.

    Returns:
        dict: The list scan results.
    """
    if debug:
        logger.debug(f"Tool: nmap_list_scan, Command: nmap {target} -sL {args}")
    return execute_scan(target, f"-sL {args}")

@mcp.tool()
def nmap_os_detection(target: str, args: str = "") -> dict:
    """
    Perform OS detection on the specified target with optional custom arguments.

    Args:
        target (str): The target IP address or hostname.
        args (str): Additional Nmap command-line arguments.

    Returns:
        dict: The OS detection results.
    """
    if debug:
        logger.debug(f"Tool: nmap_os_detection, Command: nmap {target} -O {args}")
    return execute_scan(target, f"-O {args}")

@mcp.tool()
def nmap_version_detection(target: str, args: str = "") -> dict:
    """
    Detect service versions on the specified target with optional custom arguments.

    Args:
        target (str): The target IP address or hostname.
        args (str): Additional Nmap command-line arguments.

    Returns:
        dict: The version detection results.
    """
    if debug:
        logger.debug(f"Tool: nmap_version_detection, Command: nmap {target} -sV {args}")
    return execute_scan(target, f"-sV {args}")

@mcp.tool()
def nmap_fin_scan(target: str, args: str = "") -> dict:
    """
    Perform a FIN scan on the specified target with optional custom arguments.

    Args:
        target (str): The target IP address or hostname.
        args (str): Additional Nmap command-line arguments.

    Returns:
        dict: The FIN scan results.
    """
    if debug:
        logger.debug(f"Tool: nmap_fin_scan, Command: nmap {target} -sF {args}")
    return execute_scan(target, f"-sF {args}")

@mcp.tool()
def nmap_idle_scan(target: str, args: str = "") -> dict:
    """
    Perform an idle scan on the specified target with optional custom arguments.

    Args:
        target (str): The target IP address or hostname.
        args (str): Additional Nmap command-line arguments.

    Returns:
        dict: The idle scan results.
    """
    if debug:
        logger.debug(f"Tool: nmap_idle_scan, Command: nmap {target} -sI {args}")
    return execute_scan(target, f"-sI {args}")

@mcp.tool()
def nmap_ping_scan(target: str, args: str = "") -> dict:
    """
    Perform a ping scan on the specified target with optional custom arguments.

    Args:
        target (str): The target IP address or hostname.
        args (str): Additional Nmap command-line arguments.

    Returns:
        dict: The ping scan results.
    """
    if debug:
        logger.debug(f"Tool: nmap_ping_scan, Command: nmap {target} -sn {args}")
    return execute_scan(target, f"-sn {args}")

@mcp.tool()
def nmap_syn_scan(target: str, args: str = "") -> dict:
    """
    Perform a SYN scan on the specified target with optional custom arguments.

    Args:
        target (str): The target IP address or hostname.
        args (str): Additional Nmap command-line arguments.

    Returns:
        dict: The SYN scan results.
    """
    if debug:
        logger.debug(f"Tool: nmap_syn_scan, Command: nmap {target} -sS {args}")
    return execute_scan(target, f"-sS {args}")

@mcp.tool()
def nmap_tcp_scan(target: str, args: str = "") -> dict:
    """
    Perform a TCP connect scan on the specified target with optional custom arguments.

    Args:
        target (str): The target IP address or hostname.
        args (str): Additional Nmap command-line arguments.

    Returns:
        dict: The TCP scan results.
    """
    if debug:
        logger.debug(f"Tool: nmap_tcp_scan, Command: nmap {target} -sT {args}")
    return execute_scan(target, f"-sT {args}")

@mcp.tool()
def nmap_udp_scan(target: str, args: str = "") -> dict:
    """
    Perform a UDP scan on the specified target with optional custom arguments.

    Args:
        target (str): The target IP address or hostname.
        args (str): Additional Nmap command-line arguments.

    Returns:
        dict: The UDP scan results.
    """
    if debug:
        logger.debug(f"Tool: nmap_udp_scan, Command: nmap {target} -sU {args}")
    return execute_scan(target, f"-sU {args}")

@mcp.tool()
def nmap_portscan_only(target: str, args: str = "") -> dict:
    """
    Perform a port scan only on the specified target with optional custom arguments.

    Args:
        target (str): The target IP address or hostname.
        args (str): Additional Nmap command-line arguments.

    Returns:
        dict: The port scan results.
    """
    if debug:
        logger.debug(f"Tool: nmap_portscan_only, Command: nmap {target} -sP {args}")
    return execute_scan(target, f"-sP {args}")

@mcp.tool()
def nmap_no_portscan(target: str, args: str = "") -> dict:
    """
    Perform host discovery without port scanning on the specified target with optional custom arguments.

    Args:
        target (str): The target IP address or hostname.
        args (str): Additional Nmap command-line arguments.

    Returns:
        dict: The host discovery results.
    """
    if debug:
        logger.debug(f"Tool: nmap_no_portscan, Command: nmap {target} -sn {args}")
    return execute_scan(target, f"-sn {args}")

@mcp.tool()
def nmap_arp_discovery(target: str, args: str = "") -> dict:
    """
    Perform ARP discovery on the specified target with optional custom arguments.

    Args:
        target (str): The target IP address or subnet (e.g., '192.168.1.0/24').
        args (str): Additional Nmap command-line arguments.

    Returns:
        dict: The ARP discovery results.
    """
    if debug:
        logger.debug(f"Tool: nmap_arp_discovery, Command: nmap {target} -PR {args}")
    return execute_scan(target, f"-PR {args}")

@mcp.tool()
def nmap_disable_dns_resolution(target: str, args: str = "") -> dict:
    """
    Perform a scan on the specified target with DNS resolution disabled and optional custom arguments.

    Args:
        target (str): The target IP address or hostname.
        args (str): Additional Nmap command-line arguments.

    Returns:
        dict: The scan results with DNS resolution disabled.
    """
    if debug:
        logger.debug(f"Tool: nmap_disable_dns_resolution, Command: nmap {target} -n {args}")
    return execute_scan(target, f"-n {args}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the Nmap MCP Server")
    parser.add_argument("--host", type=str, default="localhost", help="Host for the MCP SSE server")
    parser.add_argument("--port", type=int, default=8000, help="Port for the MCP SSE server")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    args = parser.parse_args()

    # Set the debug flag
    debug = args.debug
    if debug:
        logger.setLevel(logging.DEBUG)

    # Log the registered tools
    logger.info(f"Registered tools: {mcp.get_tools()}")

    # Use SSETransport to specify host and port
    mcp.run(transport="sse", host=args.host, port=args.port)
