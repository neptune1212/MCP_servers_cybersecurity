import argparse
import subprocess
from fastmcp import FastMCP
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('Dirb-MCP-Server')

debug = False

mcp = FastMCP("Dirb MCP Server")

def dirb_execute(url: str, args: str = "") -> dict:
    command = f"dirb {url} {args}"
    if debug:
        logger.debug(f"Executing command: {command}")
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        return {"output": result.stdout, "error": result.stderr}
    except subprocess.CalledProcessError as e:
        return {"output": e.stdout, "error": e.stderr}

@mcp.tool()
def dirb_basic_scan(url: str, args: str = "") -> dict:
    """
    Basic directory scan.
    """
    return dirb_execute(url, args)

@mcp.tool()
def dirb_recursive_scan(url: str, args: str = "") -> dict:
    """
    Recursive scan.
    """
    return dirb_execute(url, f"-r {args}")

@mcp.tool()
def dirb_custom_wordlist_scan(url: str, wordlist: str, extensions: str = "", args: str = "") -> dict:
    """
    Scan with custom wordlist and extensions.
    """
    ext = f"-X {extensions}" if extensions else ""
    return dirb_execute(url, f"{wordlist} {ext} {args}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the Dirb MCP Server")
    parser.add_argument("--host", type=str, default="localhost", help="Host for the MCP SSE server")
    parser.add_argument("--port", type=int, default=8095, help="Port for the MCP SSE server")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    args = parser.parse_args()

    debug = args.debug
    if debug:
        logger.setLevel(logging.DEBUG)

    logger.info(f"Registered tools: {mcp.get_tools()}")
    mcp.run(transport="sse", host=args.host, port=args.port)
