# MCP Cybersecurity Lab - Devcontainer

This environment provides a multi-container cybersecurity lab using Docker Compose, featuring a pre-configured Kali container with Cybersecurity AI (CAI) tooling.

---

## 🚀 Quick Start

### 1. Build and Start the Lab

From this directory, run:

```sh
docker compose up --build
```

This will build and start all containers: `kali-cai`, `mcp_servers`, and `metasploitable2`.

---

### 2. Enter the Kali Container

Open a new terminal and attach to the running Kali container:

```sh
docker exec -it kali-cai bash
```

---

### 3. Activate CAI and Run Autoconfiguration

Inside the container, activate the CAI Python environment and run the configuration script:

```sh
source cai/bin/activate && expect configure_cai.expect
```

This will launch CAI and automatically configure it to connect to the MCP servers for Metasploit, Nmap, and Sqlmap.

---

## 📝 Notes

- Ensure Docker is installed and running on your system.
- The `configure_cai.expect` script automates the initial CAI setup.
- After the script completes, you can interact with CAI directly.

---