# Use the official Kali Linux image as the base image
FROM kalilinux/kali-rolling

# Update and install dependencies
RUN apt-get update && \
    apt-get install -y python3-pip python3-venv metasploit-framework netcat-traditional nmap

# Create a virtual environment for metasploit
RUN python3 -m venv /opt/venv/metasploit
# Install gc-metasploit package in the virtual environment for metasploit
RUN /opt/venv/metasploit/bin/pip install gc-metasploit 

# Create a virtual environment for nmap
RUN python3 -m venv /opt/venv/nmap
# Install the required Python packages in the nmap virtual environment
RUN /opt/venv/nmap/bin/pip install python-nmap fastmcp

# Copy the Nmap MCP server script
COPY ./network/ /opt/mcp_servers/network/

# Copy the startup script
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Start the services using the startup script
CMD ["/start.sh"]
