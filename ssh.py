"""
Simple SSH checker

"""

from scapy.all import IP, TCP, sr1
from config import TARGET_IP

# Form a package: IP level + TCP level with flag "S" (SYN)
packet = IP(dst=TARGET_IP)/TCP(dport=2222, flags="S")

# Send and wait for response
reply = sr1(packet, timeout=2, verbose=0)

if reply and reply.haslayer(TCP) and reply.getlayer(TCP).flags == 0x12:
    print("Port 22 (SSH) open!")
else:
    print("Port close or not responding.")