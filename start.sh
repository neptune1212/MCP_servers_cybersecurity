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
/opt/venv/nmap/bin/python /opt/mcp_servers/network/nmap/nmap_mcp_server.py --host 0.0.0.0 --port 8086 &

# Keep the container running
tail -f /dev/null
