import socket
import threading
import logging
import os

default_server_ip = '127.0.0.1'
default_server_port = '8080'

# Configuration for the simulation
SERVER_IP = os.environ.get('SERVER_IP', default_server_ip)
SERVER_PORT = int(os.environ.get('SERVER_PORT', default_server_port))

# UDP Server to receive data from clients
def server():
    logging.basicConfig(level=logging.INFO)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind((SERVER_IP, SERVER_PORT))
        logging.debug("Server started and listening")

        while True:
            try:
                data, addr = sock.recvfrom(1024)  # Buffer size of 1024 bytes
                if not data:
                    logging.info("No response received")
                    continue

                data = data.decode()
                sensor_id, timestamp, temperature = data.split(',')
                logging.info(f"----->Received data from {sensor_id}: {temperature}°C at {timestamp}")

                # Save data in separate log files
                with open(f"{sensor_id}_log.txt", "a") as file:
                    file.write(f"{timestamp}: {temperature}\n")
            except socket.timeout:
                logging.info("No response received - socket timeout")
            except Exception as e:
                logging.error(f"Error receiving data: {e}")

# Starting the server
if __name__ == '__main__':
    server_thread = threading.Thread(target=server)
    server_thread.start()
