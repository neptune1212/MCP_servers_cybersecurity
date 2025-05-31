import argparse
import subprocess
from fastmcp import FastMCP
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('Nuclei-MCP-Server')

debug = False

mcp = FastMCP("Nuclei MCP Server")

def nuclei_execute(args: str) -> dict:
    command = f"nuclei {args}"
    if debug:
        logger.debug(f"Executing command: {command}")
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        return {"output": result.stdout, "error": result.stderr}
    except subprocess.CalledProcessError as e:
        return {"output": e.stdout, "error": e.stderr}

@mcp.tool()
def nuclei_basic_scan(target: str, template: str, args: str = "") -> dict:
    """
    Basic scan with templates.
    """
    return nuclei_execute(f"-u {target} -t {template} {args}")

@mcp.tool()
def nuclei_severity_scan(target: str, severity: str, args: str = "") -> dict:
    """
    Scan with severity filtering.
    """
    return nuclei_execute(f"-u {target} -severity {severity} {args}")

@mcp.tool()
def nuclei_headless_scan(target: str, headers: str = "", headless: bool = False, args: str = "") -> dict:
    """
    Headless mode scan with custom headers.
    """
    h = f"-H '{headers}'" if headers else ""
    hd = "-headless" if headless else ""
    return nuclei_execute(f"-u {target} {h} {hd} {args}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the Nuclei MCP Server")
    parser.add_argument("--host", type=str, default="localhost", help="Host for the MCP SSE server")
    parser.add_argument("--port", type=int, default=8092, help="Port for the MCP SSE server")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    args = parser.parse_args()

    debug = args.debug
    if debug:
        logger.setLevel(logging.DEBUG)

    logger.info(f"Registered tools: {mcp.get_tools()}")
    mcp.run(transport="sse", host=args.host, port=args.port)
