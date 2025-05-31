# Use the official Kali Linux image as the base image
FROM kalilinux/kali-rolling

# Update and install dependencies
RUN apt-get update && \
    apt-get install -y \
        commix \
        dirb \
        gobuster \
        metasploit-framework \
        netcat-traditional \
        nikto \
        nmap \
        nuclei \
        python3-pip \
        python3-venv \
        sqlmap \
        wfuzz \
        wpscan \
        wordlists \
        xsser && \
    rm -rf /var/lib/apt/lists/*

# Create a virtual environment for metasploit
RUN python3 -m venv /opt/venv/metasploit
# Install gc-metasploit package in the virtual environment for metasploit
RUN /opt/venv/metasploit/bin/pip install gc-metasploit 

# Create a virtual environment for mcp servers
RUN python3 -m venv /opt/venv/mcp_servers
# Install the required Python packages in the mcp servers virtual environment
RUN /opt/venv/mcp_servers/bin/pip install python-nmap fastmcp

# Copy the Nmap MCP server script
COPY ./mcp_servers/ /opt/mcp_servers/

# Copy the startup script
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Start the services using the startup script
CMD ["/start.sh"]
