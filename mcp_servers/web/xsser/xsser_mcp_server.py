import argparse
import subprocess
from fastmcp import FastMCP
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('XSSer-MCP-Server')

debug = False

mcp = FastMCP("XSSer MCP Server")

def xsser_execute(url: str, args: str = "") -> dict:
    command = f"xsser --url {url} {args}"
    if debug:
        logger.debug(f"Executing command: {command}")
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        return {"output": result.stdout, "error": result.stderr}
    except subprocess.CalledProcessError as e:
        return {"output": e.stdout, "error": e.stderr}

@mcp.tool()
def xsser_basic_scan(url: str, args: str = "") -> dict:
    """
    Basic XSS scan.
    """
    return xsser_execute(url, args)

@mcp.tool()
def xsser_payload_scan(url: str, payload: str, args: str = "") -> dict:
    """
    Scan with specific payloads.
    """
    return xsser_execute(url, f"--payload {payload} {args}")

@mcp.tool()
def xsser_auto_scan(url: str, args: str = "") -> dict:
    """
    Auto-inject vectors and use bypass techniques.
    """
    return xsser_execute(url, f"--auto {args}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the XSSer MCP Server")
    parser.add_argument("--host", type=str, default="localhost", help="Host for the MCP SSE server")
    parser.add_argument("--port", type=int, default=8089, help="Port for the MCP SSE server")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    args = parser.parse_args()

    debug = args.debug
    if debug:
        logger.setLevel(logging.DEBUG)

    logger.info(f"Registered tools: {mcp.get_tools()}")
    mcp.run(transport="sse", host=args.host, port=args.port)
