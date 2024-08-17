import requests
import time
import logging

# লগ সেটআপ
logging.basicConfig(filename='keep_alive.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

url = "https://testtmon.onrender.com/test"
expected_status = 200  # প্রত্যাশিত স্ট্যাটাস কোড
retry_interval = 60    # প্রাথমিক স্লিপ ইন্টারভাল (সেকেন্ডে)
max_retries = 3        # সর্বাধিক পুনরায় চেষ্টা সংখ্যা

def ping_server():
    try:
        response = requests.get(url)
        if response.status_code == expected_status:
            logging.info(f"Success: Status Code {response.status_code}, Content: {response.text}")
            return True
        else:
            logging.warning(f"Unexpected response: Status Code {response.status_code}, Content: {response.text}")
            return False
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        return False

def keep_alive():
    retries = 0
    while True:
        if ping_server():
            retries = 0  # সাফল্যের পর পুনরায় চেষ্টা সংখ্যা রিসেট করুন
        else:
            retries += 1
            if retries >= max_retries:
                logging.warning(f"Failed {retries} times, adjusting sleep interval.")
                time.sleep(retry_interval / 2)  # ব্যর্থতার ক্ষেত্রে স্লিপ ইন্টারভাল কমান
                retries = 0  # পুনরায় চেষ্টা সংখ্যা রিসেট করুন
                continue

        time.sleep(retry_interval)  # প্রতি ১ মিনিটে রিকোয়েস্ট পাঠান

if __name__ == "__main__":
    logging.info("Starting keep-alive script.")
    keep_alive()
