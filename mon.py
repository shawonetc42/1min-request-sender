import requests
import time

url = 'https://testtmon.onrender.com/test'

# রিকোয়েস্ট পাঠানোর আগে টাইম রেকর্ড করা
start_time = time.time()

# GET রিকোয়েস্ট পাঠানো
response = requests.get(url)

# রিকোয়েস্ট পাঠানোর পরে টাইম রেকর্ড করা
end_time = time.time()

# স্পিড (লেটেন্সি) নির্ণয় করা
latency = end_time - start_time

# ফলাফল প্রিন্ট করা
print(f"Status Code: {response.status_code}")
print(f"Response Time: {latency} seconds")
print(f"Response Content: {response.text[:100]}...")  # প্রথম 100 ক্যারেক্টার দেখানো হচ্ছে
