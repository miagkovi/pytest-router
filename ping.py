"""
Simple ip ping
Example output:

Router 192.168.0.1 available!
"""

import os
from config import TARGET_IP

ip = TARGET_IP
response = os.system(f"ping -c 1 {ip}") # -n for Win, -c for Linux/Mac

if response == 0:
    print(f"Router {ip} available!")
else:
    print(f"Router {ip} not available. Check cable or IP.")