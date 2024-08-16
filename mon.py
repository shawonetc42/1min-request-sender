import requests
from requests.exceptions import RequestException
import time

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

# Vercel এর জন্য Handler ফাংশন
def handler(event, context):
    send_request()
    return {
        'statusCode': 200,
        'body': 'Request sent successfully!'
    }
