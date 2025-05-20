# Use the official Kali Linux image as a base
FROM neptune1212/kali-cai:latest

# Create a directory for the application
WORKDIR /home/kali/

# User root
USER root
# Update and install dependencies
RUN apt-get update && \
    apt-get install -y expect

# Copy the configuration file into the container
COPY configure_cai.expect /home/kali/configure_cai.expect
RUN chmod +x /home/kali/configure_cai.expect

# User kali
USER kali

# Set the default command to activate the virtual environment
CMD ["/bin/bash", "-c", "source /home/kali/cai/bin/activate && bash"]
