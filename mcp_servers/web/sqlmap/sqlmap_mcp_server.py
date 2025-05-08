import argparse
import subprocess
from fastmcp import FastMCP
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('Sqlmap-MCP-Server')

# Global debug flag
debug = False

# Initialize the MCP server with a name
mcp = FastMCP("Sqlmap MCP Server")

def execute_sqlmap(target: str, args: str = "") -> dict:
    """
    Execute a sqlmap scan using the specified arguments.

    Args:
        target (str): The target URL.
        args (str): Additional sqlmap command-line arguments.

    Returns:
        dict: The scan results.
    """
    command = f"sqlmap -u {target} {args} --batch"
    if debug:
        logger.debug(f"Executing command: {command}")

    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        return {"output": result.stdout, "error": result.stderr}
    except subprocess.CalledProcessError as e:
        return {"output": e.stdout, "error": e.stderr}

@mcp.tool()
def basic_scan(target: str, args: str = "") -> dict:
    """
    Perform a basic SQL injection scan on the specified target.

    Args:
        target (str): The target URL.
        args (str): Additional sqlmap command-line arguments.

    Returns:
        dict: The scan results.
    """
    if debug:
        logger.debug(f"Tool: basic_scan, Command: sqlmap -u {target} {args}")
    return execute_sqlmap(target, args)

@mcp.tool()
def get_databases(target: str, args: str = "") -> dict:
    """
    Enumerate databases on the specified target.

    Args:
        target (str): The target URL.
        args (str): Additional sqlmap command-line arguments.

    Returns:
        dict: The enumeration results.
    """
    if debug:
        logger.debug(f"Tool: get_databases, Command: sqlmap -u {target} --dbs {args}")
    return execute_sqlmap(target, f"--dbs {args}")

@mcp.tool()
def get_tables(target: str, database: str, args: str = "") -> dict:
    """
    Enumerate tables in a specific database on the specified target.

    Args:
        target (str): The target URL.
        database (str): The database name.
        args (str): Additional sqlmap command-line arguments.

    Returns:
        dict: The enumeration results.
    """
    if debug:
        logger.debug(f"Tool: get_tables, Command: sqlmap -u {target} -D {database} --tables {args}")
    return execute_sqlmap(target, f"-D {database} --tables {args}")

@mcp.tool()
def get_columns(target: str, database: str, table: str, args: str = "") -> dict:
    """
    Enumerate columns in a specific table on the specified target.

    Args:
        target (str): The target URL.
        database (str): The database name.
        table (str): The table name.
        args (str): Additional sqlmap command-line arguments.

    Returns:
        dict: The enumeration results.
    """
    if debug:
        logger.debug(f"Tool: get_columns, Command: sqlmap -u {target} -D {database} -T {table} --columns {args}")
    return execute_sqlmap(target, f"-D {database} -T {table} --columns {args}")

@mcp.tool()
def dump_data(target: str, database: str, table: str, args: str = "") -> dict:
    """
    Dump data from a specific table on the specified target.

    Args:
        target (str): The target URL.
        database (str): The database name.
        table (str): The table name.
        args (str): Additional sqlmap command-line arguments.

    Returns:
        dict: The dump results.
    """
    if debug:
        logger.debug(f"Tool: dump_data, Command: sqlmap -u {target} -D {database} -T {table} --dump {args}")
    return execute_sqlmap(target, f"-D {database} -T {table} --dump {args}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the Sqlmap MCP Server")
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
