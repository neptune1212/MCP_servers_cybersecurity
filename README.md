# MCP Servers Cybersecurity

A comprehensive platform for running **cybersecurity MCP (Model Context Protocol) servers**, designed to integrate and expose various cybersecurity tools and frameworks as modular services. Starting with **Nmap** and **Metasploit**, this platform is containerized using Docker for ease of deployment and scalability.

---

## 📖 Overview

The MCP Servers Cybersecurity platform provides a unified interface for interacting with multiple cybersecurity tools. It leverages the **FastMCP** framework to expose these tools as modular services, enabling automation, integration, and remote execution of cybersecurity tasks.

### Current Modules

- **Nmap MCP Server**: A server exposing Nmap's powerful network scanning capabilities.
- **Metasploit RPC Server**: A server for interacting with Metasploit via RPC.

### Future Modules (Planned)

- **Burp Suite Integration**: For web application security testing.
- **OpenVAS/Greenbone**: For vulnerability scanning.
- **Wireshark/TShark**: For packet capture and analysis.
- **Custom Exploit Frameworks**: For running custom scripts and exploits.
- **Threat Intelligence Feeds**: Integration with external threat intelligence APIs.

---

## ✨ Features

- **Modular Design**: Easily add new tools and services.
- **API-Driven**: Exposes tools via RESTful APIs for seamless integration.
- **Scalable Deployment**: Containerized using Docker for portability and scalability.
- **Customizable**: Modify or extend the platform to suit your cybersecurity needs.

---

## ⚙️ Prerequisites

Ensure you have the following installed:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/MCP_servers_cybersecurity.git
cd MCP_servers_cybersecurity
```

### 2. Build and Run the Platform

Use Docker Compose to build and start the services:

```bash
docker-compose up --build
```

### 3. Access the Services

- **Nmap MCP Server**: Accessible on port 8086.
- **Metasploit RPC Server**: Accessible on port 8085.

### 4. Add New Modules

To add a new module, follow these steps:

1. Create a new directory under `network/` or a relevant folder.
2. Write the MCP server script for the tool using the FastMCP framework.
3. Update the `Dockerfile` and `start.sh` to include the new module.
4. Rebuild the Docker image using:

```bash
docker-compose up --build
```

---

## 📂 Project Structure

---

## 🌐 Environment Variables

The following environment variables can be configured in the `docker-compose.yml` file:

| Variable       | Description                          | Default Value  |
|----------------|--------------------------------------|----------------|
| MSF_PASSWORD   | Password for Metasploit RPC server  | yourpassword   |
| MSF_SERVER     | Host for Metasploit RPC server      | 127.0.0.1      |
| MSF_PORT       | Port for Metasploit RPC server      | 55553          |
| MSF_SSL        | Enable SSL for Metasploit RPC server| false          |

---

## 🛠️ Tools Provided by Nmap MCP Server

The Nmap MCP server currently exposes the following tools:

- **Top Ports Scan**: Scan the most common ports.
- **DNS Brute Force**: Discover subdomains.
- **List Scan**: List targets without scanning.
- **OS Detection**: Identify the operating system of the target.
- **Version Detection**: Detect service versions.
- **FIN Scan**: Perform a FIN scan.
- **Idle Scan**: Perform an idle scan.
- **Ping Scan**: Check if hosts are alive.
- **SYN Scan**: Perform a SYN scan.
- **TCP Scan**: Perform a TCP connect scan.
- **UDP Scan**: Perform a UDP scan.
- **Port Scan Only**: Scan for open ports.
- **No Port Scan**: Discover hosts without scanning ports.
- **ARP Discovery**: Discover hosts using ARP.
- **Disable DNS Resolution**: Scan without resolving DNS.

---

## 🔧 Customization

You can customize the platform by:

- Adding new tools as MCP modules.
- Modifying the `start.sh` script to adjust the startup behavior.
- Updating the `Dockerfile` to include additional dependencies.

---

## 🐞 Troubleshooting

### Issue: Services fail to start.

**Solution**: Ensure Docker and Docker Compose are installed and running. Check the logs using:

```bash
docker-compose logs
```

### Issue: Unable to connect to the services.

**Solution**: Verify that the ports 8085 and 8086 are not blocked by a firewall.

---

## 🗺️ Roadmap

- Add support for additional tools like Burp Suite, OpenVAS, and Wireshark.
- Implement a web-based dashboard for managing and interacting with MCP servers.
- Add support for distributed deployments across multiple nodes.

---

## 🙌 Acknowledgments

- Kali Linux for the base image.
- Metasploit Framework for penetration testing tools.
- Nmap for network scanning capabilities.
- FastMCP for the MCP server framework.
- Docker for containerization.