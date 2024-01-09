This is an API call to run iperf against an iperf server that is listening on port 5000
The API is listening on port 8000

start the API with 
uvicorn iperf_api_listen:app --host 0.0.0.0 --port 8000
