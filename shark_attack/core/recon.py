
import subprocess
import logging

def run_recon(domain):
    logging.info(f"Starting reconnaissance on {domain}")
    # Whois
    whois_data = subprocess.check_output(["whois", domain]).decode()
    print(f"WHOIS Info: {whois_data}")
    
    # DNS Enumeration
    dns_data = subprocess.check_output(["dig", domain, "ANY"]).decode()
    print(f"DNS Info: {dns_data}")
    
    logging.info(f"Reconnaissance on {domain} completed.")
