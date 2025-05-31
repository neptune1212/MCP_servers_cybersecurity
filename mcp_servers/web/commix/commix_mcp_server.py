import argparse
import subprocess
from fastmcp import FastMCP
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('Commix-MCP-Server')

debug = False

mcp = FastMCP("Commix MCP Server")

def commix_execute(url: str, args: str = "") -> dict:
    command = f"commix --url {url} {args}"
    if debug:
        logger.debug(f"Executing command: {command}")
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        return {"output": result.stdout, "error": result.stderr}
    except subprocess.CalledProcessError as e:
        return {"output": e.stdout, "error": e.stderr}

@mcp.tool()
def commix_basic_scan(url: str, args: str = "") -> dict:
    """
    Basic command injection scan.
    """
    return commix_execute(url, args)

@mcp.tool()
def commix_technique_scan(url: str, technique: str, args: str = "") -> dict:
    """
    Scan with specific techniques.
    """
    return commix_execute(url, f"--technique={technique} {args}")

@mcp.tool()
def commix_os_shell(url: str, args: str = "") -> dict:
    """
    Automated exploitation with OS shell.
    """
    return commix_execute(url, f"--os-shell {args}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the Commix MCP Server")
    parser.add_argument("--host", type=str, default="localhost", help="Host for the MCP SSE server")
    parser.add_argument("--port", type=int, default=8088, help="Port for the MCP SSE server")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    args = parser.parse_args()

    debug = args.debug
    if debug:
        logger.setLevel(logging.DEBUG)

    logger.info(f"Registered tools: {mcp.get_tools()}")
    mcp.run(transport="sse", host=args.host, port=args.port)
