# Network Scanner Script

This Python script performs network scanning to detect active devices and open ports on a specified network.

## Dependencies

- Python 3.12
- Required Python packages: `socket`, `requests`

## Script Overview

The script includes two main functions:
- `get_local_ip()`: Retrieves the local IP address of the machine.
- `get_public_ip()`: Retrieves the public IP address of the machine using an external API (`https://api.ipify.org`).

## Usage

1. **Install Dependencies:**
   ```bash
   pip install requests

2. **Run the Script:**
 ```bash
   python check_ip.py

1. **Excepted Outcome:**
   ```bash
   Local IP Address: 192.168.56.1
   Public IP Address: 102.88.70.11


### How to Run the network_scanner.py:
1. **Create a Script**: Create a script as `network_scanner.py`.
   
2. **Install Dependencies**: Open a terminal and install the required `requests` library using:
   ```bash
   pip install scapy
   pip install sockets


3. **Run the Script**: Execute the script using Python:
    ```bash
    python check_ip.py


4. **Expected Output**: The script will scan the specified IP addresses (`192.168.1.1` and `192.168.1.10`) for open ports and write the results to `scan_results.txt`.
    ```bash
   Scan Results:
    [+] 192.168.1.1 is up
    No open ports found
    [+] 192.168.1.10 is up
    No open ports found



#
