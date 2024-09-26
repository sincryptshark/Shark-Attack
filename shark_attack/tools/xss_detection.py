
import requests
import logging

def check_xss(url):
    logging.info(f"Checking XSS on {url}")
    
    payload = "<script>alert('XSS')</script>"
    test_url = f"{url}?q={payload}"

    try:
        response = requests.get(test_url)
        if payload in response.text:
            print("[+] XSS vulnerability detected!")
            logging.info("[+] XSS vulnerability detected!")
        else:
            print("[-] No XSS vulnerability found.")
            logging.info("[-] No XSS vulnerability found.")
    except Exception as e:
        logging.error(f"Error checking XSS: {e}")
