import requests

# The URL where your FastAPI app is running
url = 'http://192.168.0.154:8000/run-iperf'

# Example iperf parameters - you can modify these based on your requirement
server_ip = '192.168.0.42'
duration = 1

# Construct the URL with query parameters
url_with_params = f"{url}?server_ip={server_ip}&duration={duration}"

# Making a POST request to the iperf endpoint
response = requests.post(url_with_params)

# Printing the response
print("Status Code:", response.status_code)
print("Response:", response.json())
