import socket

# Define the target IP addresses to scan
targets = ["192.168.1.1", "192.168.1.10"]

# Function to perform port scan
def port_scan(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            return True
        else:
            return False
        sock.close()
    except socket.error:
        return False

# Function to scan ports for a given IP
def scan_ports(ip):
    open_ports = []
    for port in [22, 80, 443]:  # Specify the ports to scan here
        if port_scan(ip, port):
            open_ports.append(port)
    return open_ports

# Main function to initiate the scanning process
def main():
    with open("scan_results.txt", "w") as f:
        f.write("Scan Results:\n")
        
        # Iterate over each target IP
        for ip in targets:
            open_ports = scan_ports(ip)
            if open_ports:
                f.write(f"[+] {ip} is up\n")
                f.write(f"    Open ports: {open_ports}\n")
                print(f"[+] {ip} is up")
                print(f"    Open ports: {open_ports}")
            else:
                f.write(f"[+] {ip} is up\n")
                f.write(f"    No open ports found\n")
                print(f"[+] {ip} is up")
                print(f"    No open ports found")

if __name__ == "__main__":
    main()
