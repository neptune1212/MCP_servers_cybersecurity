import argparse
import subprocess
from fastmcp import FastMCP
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('Gobuster-MCP-Server')

debug = False

mcp = FastMCP("Gobuster MCP Server")

def gobuster_execute(mode: str, args: str) -> dict:
    command = f"gobuster {mode} {args}"
    if debug:
        logger.debug(f"Executing command: {command}")
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        return {"output": result.stdout, "error": result.stderr}
    except subprocess.CalledProcessError as e:
        return {"output": e.stdout, "error": e.stderr}

@mcp.tool()
def gobuster_dir_scan(url: str, wordlist: str, args: str = "") -> dict:
    """
    Directory brute-forcing.
    """
    return gobuster_execute("dir", f"-u {url} -w {wordlist} {args}")

@mcp.tool()
def gobuster_dns_scan(domain: str, wordlist: str, args: str = "") -> dict:
    """
    DNS subdomain enumeration.
    """
    return gobuster_execute("dns", f"-d {domain} -w {wordlist} {args}")

@mcp.tool()
def gobuster_vhost_scan(domain: str, wordlist: str, args: str = "") -> dict:
    """
    Virtual host brute-forcing.
    """
    return gobuster_execute("vhost", f"-u {domain} -w {wordlist} {args}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the Gobuster MCP Server")
    parser.add_argument("--host", type=str, default="localhost", help="Host for the MCP SSE server")
    parser.add_argument("--port", type=int, default=8094, help="Port for the MCP SSE server")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    args = parser.parse_args()

    debug = args.debug
    if debug:
        logger.setLevel(logging.DEBUG)

    logger.info(f"Registered tools: {mcp.get_tools()}")
    mcp.run(transport="sse", host=args.host, port=args.port)
