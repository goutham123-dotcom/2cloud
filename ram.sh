#!/bin/bash

# Calculate system RAM
ram=$(free -h | awk '/^Mem:/ {print $2}')

# Create a service
sudo bash -c "echo '[Unit]
Description=Display system RAM

[Service]
ExecStart=/bin/bash -c \"echo System RAM: $ram\"
Restart=always
User=root

[Install]
WantedBy=multi-user.target' > /etc/systemd/system/display-ram.service"

# Reload systemd configuration
sudo systemctl daemon-reload

# Enable the service
sudo systemctl enable display-ram.service

# Start the service
sudo systemctl start display-ram.service
