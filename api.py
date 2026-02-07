import requests
from requests.auth import HTTPBasicAuth

url = "https://192.168.1.1/restconf/data/interfaces"
headers = {"Accept": "application/yang-data+json"}

# Ignore SSL (lab)
response = requests.get(url, 
                        auth=HTTPBasicAuth('admin', 'password123'), 
                        headers=headers, 
                        verify=False)

if response.status_code == 200:
    print("Data received:", response.json())
else:
    print(f"Error: {response.status_code}")