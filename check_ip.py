import socket
import requests

def get_local_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        public_ip = response.json()['ip']
        return public_ip
    except requests.RequestException as e:
        return str(e)

if __name__ == "__main__":
    print(f"Local IP Address: {get_local_ip()}")
    print(f"Public IP Address: {get_public_ip()}")
