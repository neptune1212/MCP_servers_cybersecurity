import argparse
import subprocess
from fastmcp import FastMCP
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('WPScan-MCP-Server')

debug = False

mcp = FastMCP("WPScan MCP Server")

def wpscan_execute(target: str, args: str = "") -> dict:
    command = f"wpscan --url {target} {args}"
    if debug:
        logger.debug(f"Executing command: {command}")
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        return {"output": result.stdout, "error": result.stderr}
    except subprocess.CalledProcessError as e:
        return {"output": e.stdout, "error": e.stderr}

@mcp.tool()
def wpscan_basic_scan(target: str, args: str = "") -> dict:
    """
    Perform a basic WPScan scan on the specified target.
    """
    return wpscan_execute(target, args)

@mcp.tool()
def wpscan_vuln_scan(target: str, api_token: str, args: str = "") -> dict:
    """
    Scan with vulnerability detection using API token.
    """
    return wpscan_execute(target, f"--api-token {api_token} {args}")

@mcp.tool()
def wpscan_enumerate(target: str, enum_type: str = "u,ap,at", args: str = "") -> dict:
    """
    Enumerate users, plugins, and themes.
    """
    return wpscan_execute(target, f"--enumerate {enum_type} {args}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the WPScan MCP Server")
    parser.add_argument("--host", type=str, default="localhost", help="Host for the MCP SSE server")
    parser.add_argument("--port", type=int, default=8090, help="Port for the MCP SSE server")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    args = parser.parse_args()

    debug = args.debug
    if debug:
        logger.setLevel(logging.DEBUG)

    logger.info(f"Registered tools: {mcp.get_tools()}")
    mcp.run(transport="sse", host=args.host, port=args.port)
