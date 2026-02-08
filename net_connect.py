from netmiko import ConnectHandler
from config import ROUTER_IP, SSH_PORT, SSH_PASSWORD

# Connection data
device = {
    'device_type': 'cisco_ios', # router type
    'host': ROUTER_IP,
    'username': 'admin',
    'password': SSH_PASSWORD,
}

# Connection status request
with ConnectHandler(**device) as net_connect:
    output = net_connect.send_command('show ip interface brief')
    print(output)