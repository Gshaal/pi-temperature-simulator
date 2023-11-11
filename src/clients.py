import socket
import time
import os
import random
import threading

SERVER_IP = os.environ['SERVER_IP']
SERVER_PORT = int(os.environ['SERVER_PORT'])
SENSOR_IDS = ["Sensor1", "Sensor2", "Sensor3"]

# UDP Client representing a sensor
def client(sensor_id):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        while True:
            # Simulating temperature reading
            temperature = generateCleintResponse() 
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            message = f"{sensor_id},{timestamp},{temperature}"
            sock.sendto(message.encode(), (SERVER_IP, SERVER_PORT))
            time.sleep(5)  # Sending data every 5 seconds

def generateCleintResponse(min_temp=-10, max_temp=40):
    return round(random.uniform(min_temp, max_temp), 2)


# Starting the 
if __name__ == '__main__':
    client_threads = []
    for sensor_id in SENSOR_IDS:
        thread = threading.Thread(target=client, args=(sensor_id,))
        thread.start()
        client_threads.append(thread)