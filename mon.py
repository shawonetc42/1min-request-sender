from flask import Flask
import requests
import threading
import time

app = Flask(__name__)

url = 'https://testtmon.onrender.com/test'

def send_request():
    try:
        response = requests.get(url)
        print(f'Request sent: {response.status_code} - {response.text}')
    except requests.RequestException as e:
        print(f'Error: {e}')

def start_request_loop():
    seconds_in_24_hours = 24 * 60 * 60
    start_time = time.time()
    
    while time.time() - start_time < seconds_in_24_hours:
        send_request()
        time.sleep(60)  # Wait for 60 seconds

@app.route('/')
def home():
    return "Request loop is running in the background!"

if __name__ == '__main__':
    # Start the request loop in a background thread
    threading.Thread(target=start_request_loop).start()
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)
