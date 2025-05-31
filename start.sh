#!/bin/bash

# Start the Metasploit RPC server
msfrpcd -P $MSF_PASSWORD -S -a $MSF_SERVER -p $MSF_PORT

# Wait for the Metasploit RPC server to be ready
until nc -z $MSF_SERVER $MSF_PORT; do
  echo "Waiting for Metasploit RPC server to be ready..."
  sleep 2
done

# Start gc-metasploit
/opt/venv/metasploit/bin/gc-metasploit --transport http --host 0.0.0.0 --port 8085 &

# Start the Nmap MCP server
/opt/venv/mcp_servers/bin/python /opt/mcp_servers/network/nmap/nmap_mcp_server.py --host 0.0.0.0 --port 8086 --debug &

# Start the Sqlmap MCP server
/opt/venv/mcp_servers/bin/python /opt/mcp_servers/web/sqlmap/sqlmap_mcp_server.py --host 0.0.0.0 --port 8096 --debug &

# Start the Nikto MCP server
/opt/venv/mcp_servers/bin/python /opt/mcp_servers/web/nikto/nikto_mcp_server.py --host 0.0.0.0 --port 8093 --debug &

# Start the WPScan MCP server
/opt/venv/mcp_servers/bin/python /opt/mcp_servers/web/wpscan/wpscan_mcp_server.py --host 0.0.0.0 --port 8090 --debug &

# Start the Gobuster MCP server
/opt/venv/mcp_servers/bin/python /opt/mcp_servers/web/gobuster/gobuster_mcp_server.py --host 0.0.0.0 --port 8094 --debug &

# Start the Dirb MCP server
/opt/venv/mcp_servers/bin/python /opt/mcp_servers/web/dirb/dirb_mcp_server.py --host 0.0.0.0 --port 8095 --debug &

# Start the Wfuzz MCP server
/opt/venv/mcp_servers/bin/python /opt/mcp_servers/web/wfuzz/wfuzz_mcp_server.py --host 0.0.0.0 --port 8091 --debug &

# Start the Nuclei MCP server
/opt/venv/mcp_servers/bin/python /opt/mcp_servers/web/nuclei/nuclei_mcp_server.py --host 0.0.0.0 --port 8092 --debug &

# Start the Commix MCP server
/opt/venv/mcp_servers/bin/python /opt/mcp_servers/web/commix/commix_mcp_server.py --host 0.0.0.0 --port 8088 --debug &

# Start the XSSer MCP server
/opt/venv/mcp_servers/bin/python /opt/mcp_servers/web/xsser/xsser_mcp_server.py --host 0.0.0.0 --port 8089 --debug &

# Keep the container running
tail -f /dev/null
