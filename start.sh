#!/bin/bash

export SERVER_IP="127.0.0.1"
export SERVER_PORT=8080
echo "SERVER_IP is set to: $SERVER_IP"
echo "SERVER_PORT is set to: $SERVER_PORT"


# Find the process ID of the server script
PID=$(ps aux | grep 'server.py' | grep -v grep | awk '{print $2}')

# Check if the PID is found
if [ -z "$PID" ]; then
    echo "Server is not running."
else
    # Kill the server process
    kill $PID
    echo "Server stopped."
fi

# Update package list and upgrade existing packages
sudo apt-get update
sudo apt-get upgrade -y

# Check if Python3 is installed
if ! command -v python3 &> /dev/null
then
    echo "ERROR: Python 3 is not installed"
else
    echo "Python 3 is already installed."
fi


# Run the server
python3 src/server.py &

sleep 2

# Run the client and opt in to server logs
python3 src/clients.py > /dev/null 2>&1 &