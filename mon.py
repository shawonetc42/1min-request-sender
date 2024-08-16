import requests
import time

url = "https://testtmon.onrender.com/test"

while True:
    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}, Content: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    
    time.sleep(60)  # ১ মিনিট অপেক্ষা করুন
