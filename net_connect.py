from netmiko import ConnectHandler

# Connection data
device = {
    'device_type': 'cisco_ios', # router type
    'host': 'localhost',
    'username': 'admin',
    'password': 'admin',
}

# Connection status request
with ConnectHandler(**device) as net_connect:
    output = net_connect.send_command('show ip interface brief')
    print(output)