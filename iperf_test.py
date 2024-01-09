import requests

# The URL where your FastAPI app is running
url = 'http://192.168.0.154:8000/run-iperf'

# Example iperf parameters - you can modify these based on your requirement
server_ip = '192.168.0.42'
duration = 13

params = {
    'server_ip': server_ip,
    'duration': duration
}

response = requests.post(url, params=params)

# Printing the response
print("Status Code:", response.status_code)
print("Response:", response.json())

