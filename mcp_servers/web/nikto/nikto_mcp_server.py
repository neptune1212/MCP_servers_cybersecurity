import argparse
import subprocess
from fastmcp import FastMCP
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('Nikto-MCP-Server')

debug = False

mcp = FastMCP("Nikto MCP Server")

def nikto_execute_nikto(target: str, args: str = "") -> dict:
    """
    Execute a Nikto scan using the specified arguments.

    Args:
        target (str): The target URL or IP.
        args (str): Additional Nikto command-line arguments.

    Returns:
        dict: The scan results.
    """
    command = f"nikto -h {target} {args}"
    if debug:
        logger.debug(f"Executing command: {command}")
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        return {"output": result.stdout, "error": result.stderr}
    except subprocess.CalledProcessError as e:
        return {"output": e.stdout, "error": e.stderr}

@mcp.tool()
def nikto_basic_scan(target: str, args: str = "") -> dict:
    """
    Perform a basic Nikto scan on the specified target.

    Args:
        target (str): The target URL or IP.
        args (str): Additional Nikto command-line arguments.

    Returns:
        dict: The scan results.
    """
    if debug:
        logger.debug(f"Tool: nikto_basic_scan, Command: nikto -h {target} {args}")
    return nikto_execute_nikto(target, args)

@mcp.tool()
def nikto_ssl_scan(target: str, args: str = "") -> dict:
    """
    Perform an SSL-specific Nikto scan.

    Args:
        target (str): The target URL or IP.
        args (str): Additional Nikto command-line arguments.

    Returns:
        dict: The scan results.
    """
    if debug:
        logger.debug(f"Tool: nikto_ssl_scan, Command: nikto -h {target} -ssl {args}")
    return nikto_execute_nikto(target, f"-ssl {args}")

@mcp.tool()
def nikto_scan_with_plugins(target: str, plugins: str, args: str = "") -> dict:
    """
    Run Nikto scan with specified plugins.

    Args:
        target (str): The target URL or IP.
        plugins (str): Comma-separated list of plugins.
        args (str): Additional Nikto command-line arguments.

    Returns:
        dict: The scan results.
    """
    if debug:
        logger.debug(f"Tool: nikto_scan_with_plugins, Command: nikto -h {target} -Plugins {plugins} {args}")
    return nikto_execute_nikto(target, f"-Plugins {plugins} {args}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the Nikto MCP Server")
    parser.add_argument("--host", type=str, default="localhost", help="Host for the MCP SSE server")
    parser.add_argument("--port", type=int, default=8093, help="Port for the MCP SSE server")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    args = parser.parse_args()

    debug = args.debug
    if debug:
        logger.setLevel(logging.DEBUG)

    logger.info(f"Registered tools: {mcp.get_tools()}")

    mcp.run(transport="sse", host=args.host, port=args.port)
