
import requests
import logging

def check_sql_injection(url):
    logging.info(f"Checking SQL Injection on {url}")
    
    payload = "' OR '1'='1"
    test_url = f"{url}?id={payload}"

    try:
        response = requests.get(test_url)
        if "mysql" in response.text.lower() or "syntax" in response.text.lower():
            print("[+] SQL Injection vulnerability detected!")
            logging.info("[+] SQL Injection vulnerability detected!")
        else:
            print("[-] No SQL Injection vulnerability found.")
            logging.info("[-] No SQL Injection vulnerability found.")
    except Exception as e:
        logging.error(f"Error checking SQL Injection: {e}")
