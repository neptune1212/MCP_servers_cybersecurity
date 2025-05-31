import argparse
import subprocess
from fastmcp import FastMCP
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('Wfuzz-MCP-Server')

debug = False

mcp = FastMCP("Wfuzz MCP Server")

def wfuzz_execute(args: str) -> dict:
    command = f"wfuzz {args}"
    if debug:
        logger.debug(f"Executing command: {command}")
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        return {"output": result.stdout, "error": result.stderr}
    except subprocess.CalledProcessError as e:
        return {"output": e.stdout, "error": e.stderr}

@mcp.tool()
def wfuzz_basic_fuzz(url: str, wordlist: str, args: str = "") -> dict:
    """
    Basic fuzzing.
    """
    return wfuzz_execute(f"-w {wordlist} -u {url} {args}")

@mcp.tool()
def wfuzz_multi_injection(url: str, wordlists: list, args: str = "") -> dict:
    """
    Fuzzing with multiple injection points.
    """
    wl_args = ' '.join([f"-w {w}" for w in wordlists])
    return wfuzz_execute(f"{wl_args} -u {url} {args}")

@mcp.tool()
def wfuzz_custom_headers(url: str, wordlist: str, headers: str = "", args: str = "") -> dict:
    """
    Fuzzing with custom headers and authentication.
    """
    h = f"-H '{headers}'" if headers else ""
    return wfuzz_execute(f"-w {wordlist} -u {url} {h} {args}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the Wfuzz MCP Server")
    parser.add_argument("--host", type=str, default="localhost", help="Host for the MCP SSE server")
    parser.add_argument("--port", type=int, default=8091, help="Port for the MCP SSE server")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    args = parser.parse_args()

    debug = args.debug
    if debug:
        logger.setLevel(logging.DEBUG)

    logger.info(f"Registered tools: {mcp.get_tools()}")
    mcp.run(transport="sse", host=args.host, port=args.port)
