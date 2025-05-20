# Use the official Kali Linux image as a base
FROM neptune1212/kali-cai:latest

# Update and install dependencies
RUN apt-get update && \
    apt-get install -y git python3-pip python3-venv sudo && \
    apt-get install -y kali-linux-headless kali-linux-large

# Create a directory for the application
WORKDIR /home/kali/

# Copy the configuration file into the container
COPY configure_cai.expect /home/kali/configure_cai.expect
RUN chmod +x /home/kali/configure_cai.expect

# Set the default command to activate the virtual environment
CMD ["/bin/bash", "-c", "source /home/kali/cai/bin/activate && bash"]
