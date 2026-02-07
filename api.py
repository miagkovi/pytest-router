import requests
from requests.auth import HTTPBasicAuth

url = "http://localhost:8080/"
headers = {"Accept": "application/yang-data+json"}

# Ignore SSL (lab)
response = requests.get(url, 
                        auth=HTTPBasicAuth('admin', 'admin'), 
                        headers=headers, 
                        verify=False)

if response.status_code == 200:
    print("Data received:", response.text)
else:
    print(f"Error: {response.status_code}")