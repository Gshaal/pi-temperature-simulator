# Python UDP Server and Client Setup Guide

## Overview
This README provides detailed instructions for setting up and running a Python UDP server and client on an Ubuntu machine. this project create server that receive temperature data from clients, process it, and potentially log and display it.

## About the UDP Server
The Python UDP server is designed to handle incoming temperature data from multiple clients. Each client sends data packets containing temperature readings along with a timestamp and a sensor ID. The server listens for these packets, processes them, and can perform actions such as logging the data to files or displaying it in real-time.

## Use-Cases
- Environmental monitoring in agriculture, laboratories, data centers, etc.
- IoT applications requiring real-time temperature monitoring.
- Research projects needing to gather and analyze temperature data.

## Requirements
- **Ubuntu Operating System**: 22.04.2 LTS
- **Python 3.x**: Python 3.10.12

## Installation and Setup

### Cloning the Repository
If the server and client scripts are hosted in a GitHub repository, start by cloning the repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

### Running the Server and Client
Ensure you are in the directory containing the start.sh script.
Run the script to start the server and client.
```bash
./start.sh
```
This script starts the Python UDP server and clients set in `SENSOR_IDS` and opt in to server to see logs

### Stopping the Server
To stop the server:
```bash
./stop.sh
```
