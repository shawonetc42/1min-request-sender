# api/check_server.py
import requests
import time

def handler(request):
    url = 'https://testtmon.onrender.com/test'

    try:
        # রিকোয়েস্ট পাঠানোর আগে টাইম রেকর্ড করা
        start_time = time.time()

        # GET রিকোয়েস্ট পাঠানো
        response = requests.get(url)

        # রিকোয়েস্ট পাঠানোর পরে টাইম রেকর্ড করা
        end_time = time.time()

        # স্পিড (লেটেন্সি) নির্ণয় করা
        latency = end_time - start_time

        # ফলাফল প্রস্তুত করা
        result = {
            "status_code": response.status_code,
            "response_time": f"{latency:.2f} seconds",
            "response_content": response.text[:100] + "..."
        }
    except requests.exceptions.RequestException as e:
        result = {"error": str(e)}

    return {
        "statusCode": 200,
        "body": result
    }
