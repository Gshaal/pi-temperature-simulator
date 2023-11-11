import socket
import time
import threading
import os

# Configuration for the simulation
SERVER_IP = os.environ['SERVER_IP']
SERVER_PORT = int(os.environ['SERVER_PORT'])




# UDP Server to receive data from clients
def server():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind((SERVER_IP, SERVER_PORT))
        print("Server started and listening")

        while True:
            data, addr = sock.recvfrom(1024)  # Buffer size of 1024 bytes
            data = data.decode()
            sensor_id, timestamp, temperature = data.split(',')
            print(f"Received data from {sensor_id}: {temperature}°C at {timestamp}")

            # Save data in separate log files
            with open(f"{sensor_id}_log.txt", "a") as file:
                file.write(f"{timestamp}: {temperature}\n")

# Starting the server
if __name__ == '__main__':
    server_thread = threading.Thread(target=server)
    server_thread.start()


