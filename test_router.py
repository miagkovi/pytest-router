import pytest
import os
import requests
import socket

from config import ROUTER_IP, HTTP_PORT, SSH_PORT

def test_ping_router():
    """L3 level: Testing if router is pingable using os.system and ping command"""
    # -c 1 for Linux/WSL, -n 1 for Windows
    response = os.system(f"ping -c 1 {ROUTER_IP}")
    assert response == 0, f"Router {ROUTER_IP} not pingable"

def test_http_web_interface():
    """L7 level: Testing if HTTP web interface is responsive"""
    url = f"http://{ROUTER_IP}:{HTTP_PORT}"
    try:
        response = requests.get(url, timeout=5)
        assert response.status_code == 200
        assert "Service" in response.text or "Welcome" in response.text
    except requests.exceptions.RequestException as e:
        pytest.fail(f"HTTP request failed: {e}")

def test_ssh_port_open():
    """L4 level: testing if SSH port is open using socket"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    result = sock.connect_ex((ROUTER_IP, SSH_PORT))
    sock.close()
    assert result == 0, f"SSH port ({SSH_PORT}) CLOSED or not responding"