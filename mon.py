import requests
import time

url = 'https://testtmon.onrender.com/test'

def send_request():
    try:
        response = requests.get(url)
        print(f'Request sent: {response.status_code} - {response.text}')
    except requests.RequestException as e:
        print(f'Error: {e}')

# 24 hours in seconds
seconds_in_24_hours = 24 * 60 * 60

start_time = time.time()

while time.time() - start_time < seconds_in_24_hours:
    send_request()
    time.sleep(60)  # Wait for 60 seconds
