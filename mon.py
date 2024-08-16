import requests
import time
from requests.exceptions import RequestException

# সাইটের URL
url = "https://testtmon.onrender.com/test"

def send_request():
    try:
        response = requests.get(url, timeout=10)  # টাইমআউট ১০ সেকেন্ডে সেট করা হয়েছে
        response.raise_for_status()  # যদি স্ট্যাটাস কোড ২০০ না হয় তাহলে এ্যারর তুলবে
        print(f"Status Code: {response.status_code}, Content: {response.json()}")
    except RequestException as e:
        print(f"An error occurred: {e}")
        # ৫ সেকেন্ড পরে পুনরায় চেষ্টা করবে
        time.sleep(5)
        send_request()

def main():
    while True:
        send_request()
        time.sleep(60)  # ১ মিনিট পর পুনরায় রিকুয়েস্ট পাঠাবে

if __name__ == "__main__":
    main()
