from netmiko import ConnectHandler

# Connection data
device = {
    'device_type': 'cisco_ios', # router type
    'host': '192.168.1.1',
    'username': 'admin',
    'password': 'password123',
}

# Connection status request
with ConnectHandler(**device) as net_connect:
    output = net_connect.send_command('show ip interface brief')
    print(output)