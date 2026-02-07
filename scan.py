"""
Simple router TCP port scanner
Example output:

Scanning 192.168.0.1...

Port 22 (SSH): OPEN
Port 23 (Telnet): CLOSE
Port 80 (HTTP): OPEN
Port 443 (HTTPS): CLOSE
Port 53 (DNS): CLOSE
"""

import socket
from config import TARGET_IP

target_ip = TARGET_IP
# List of ports to check:
ports = {
    2222: "SSH",
    2323: "Telnet",
    8080: "HTTP",
    8443: "HTTPS",
    }

print(f"Scanning {target_ip}...\n")

for port, name in ports.items():
    # Create socket (AF_INET - IPv4, SOCK_STREAM - TCP)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1) # wait 1 ms max
    result = sock.connect_ex((target_ip, port)) # 0 if port open
    
    status = "OPEN" if result == 0 else "CLOSED"
    print(f"Port {port} ({name}): {status}")
    sock.close()