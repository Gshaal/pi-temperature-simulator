# Find the process ID of the server script
PID=$(ps aux | grep 'server.py' | grep -v grep | awk '{print $2}')

# Find the process ID of the client script
PID2=$(ps aux | grep 'clients.py' | grep -v grep | awk '{print $2}')

PID3=$(ps aux | grep 'server_spec.py' | grep -v grep | awk '{print $2}')



# Check if the PID is found
if [ -z "$PID" ]; then
    echo "Server is not running."
    echo
else
    # Kill the server process
    kill $PID
    echo "Server stopped."
    
fi

# Check if the PID is found
if [ -z "$PID2" ]; then
    echo "client is not running."
    echo
else
    # Kill the server process
    kill $PID2
    echo "client stopped."
    
fi

if [ -z "$PID3" ]; then
    echo "client2 is not running."
    echo
else
    # Kill the server process
    kill $PID3
    echo "client2 stopped."
    
fi