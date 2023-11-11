# Find the process ID of the server script
SERVER_PID=$(ps aux | grep 'server.py' | grep -v grep | awk '{print $2}')

# Find the process ID of the client script
CLIENT_PID=$(ps aux | grep 'clients.py' | grep -v grep | awk '{print $2}')





# Check if the SERVER_PID is found
if [ -z "$SERVER_PID" ]; then
    echo "Server is not running."
    echo
else
    # Kill the server process
    kill $SERVER_PID
    echo "Server stopped."
    
fi

# Check if the CLIENT_PID is found
if [ -z "$CLIENT_PID" ]; then
    echo "client is not running."
    echo
else
    # Kill the client process
    kill $CLIENT_PID
    echo "client stopped."
    
fi

