import requests
import time

# আপনার Vercel এন্ডপইন্টের URL
url = 'https://1min-request-sender.vercel.app/'

def send_request():
    start_time = time.time()

    try:
        response = requests.get(url)
        latency = time.time() - start_time
        print(f"Status Code: {response.status_code}")
        print(f"Response Time: {latency:.2f} seconds")
        print(f"Response Content: {response.text[:100]}...")  # প্রথম 100 ক্যারেক্টার
    except Exception as e:
        print(f"Request failed: {e}")

# প্রতি মিনিটে রিকোয়েস্ট পাঠান
while True:
    send_request()
    time.sleep(60)  # 60 সেকেন্ড অপেক্ষা করুন
