#!/bin/bash

# Get total system RAM
ram=$(free -m | awk 'NR==2{print $2}')

# Save to file
echo $ram > /tmp/system_ram.txt


