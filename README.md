# MCP Servers Cybersecurity

A platform for running **cybersecurity MCP (Model Context Protocol) servers**, integrating tools like **Nmap**, **Metasploit**, and **Sqlmap** as modular services. The platform is containerized using Docker for easy deployment and scalability.

---

## 📖 Overview

The MCP Servers Cybersecurity platform provides a unified interface for interacting with multiple cybersecurity tools. It uses the **FastMCP** framework to expose these tools as modular services, enabling automation, integration, and remote execution of cybersecurity tasks.

### Current Modules

- **Nmap MCP Server**: Exposes Nmap's network scanning capabilities.
- **Metasploit RPC Server**: Enables interaction with Metasploit via RPC.
- **Sqlmap MCP Server**: Provides SQL injection testing capabilities.

### Planned Modules

- **Burp Suite**: Web application security testing.
- **OpenVAS/Greenbone**: Vulnerability scanning.
- **Wireshark/TShark**: Packet capture and analysis.
- **Custom Exploit Frameworks**: Running custom scripts and exploits.
- **Threat Intelligence Feeds**: Integration with external APIs.

---

## ✨ Features

- **Modular Design**: Add new tools and services easily.
- **API-Driven**: RESTful APIs for seamless integration.
- **Scalable Deployment**: Dockerized for portability and scalability.
- **Customizable**: Extend the platform to fit your needs.

---

## ⚙️ Prerequisites

Ensure the following are installed:

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

- **Nmap MCP Server**: Port 8086  
- **Metasploit RPC Server**: Port 8085  
- **Sqlmap MCP Server**: Port 8087  

### 4. Add New Modules

1. Create a new directory under `network/` or a relevant folder.  
2. Write the MCP server script using the FastMCP framework.  
3. Update the `Dockerfile` and `start.sh` to include the new module.  
4. Rebuild the Docker image:

```bash
docker-compose build
```

---

## 📂 Project Structure

- **network/**: Contains MCP server modules.  
- **docker-compose.yml**: Configuration for Docker Compose.  
- **start.sh**: Startup script for initializing services.  

---

## 🌐 Environment Variables

Configure these in `docker-compose.yml`:

| Variable       | Description                          | Default Value  |
|----------------|--------------------------------------|----------------|
| `MSF_PASSWORD` | Password for Metasploit RPC server   | `yourpassword` |
| `MSF_SERVER`   | Host for Metasploit RPC server       | `127.0.0.1`    |
| `MSF_PORT`     | Port for Metasploit RPC server       | `55553`        |
| `MSF_SSL`      | Enable SSL for Metasploit RPC server | `false`        |

---

## 🛠️ Tools Provided

### Nmap MCP Server

- Top Ports Scan  
- DNS Brute Force  
- OS Detection  
- Version Detection  
- SYN Scan  
- TCP Scan  
- UDP Scan  

### Sqlmap MCP Server

- Basic Scan  
- Get Databases  
- Get Tables  
- Get Columns  
- Dump Data  

---

## 🔧 Customization

- Add new tools as MCP modules.  
- Modify `start.sh` for custom startup behavior.  
- Update the `Dockerfile` for additional dependencies.  

---

## 🐞 Troubleshooting

- **Services fail to start**: Ensure Docker and Docker Compose are installed and running. Check logs using:

    ```bash
    docker-compose logs
    ```

- **Unable to connect to services**: Verify ports 8085, 8086, and 8087 are not blocked by a firewall.

---

## 🗺️ Roadmap

- Add support for Burp Suite, OpenVAS, and Wireshark.  
- Implement a web-based dashboard for managing MCP servers.  
- Support distributed deployments across multiple nodes.  

---

## 🙌 Acknowledgments

- **Kali Linux**: Base image.  
- **Metasploit Framework**: Penetration testing tools.  
- **Nmap**: Network scanning capabilities.  
- **Sqlmap**: SQL injection testing.  
- **FastMCP**: MCP server framework.  
- **Docker**: Containerization.  