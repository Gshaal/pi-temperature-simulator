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