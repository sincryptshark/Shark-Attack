
import argparse
import json
import logging
from core import scanner, recon, exploit, post_exploit, reporting
from tools import sql_injection, xss_detection, privilege_escalation
from core.error_handler import handle_error

# Load configuration file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

def setup_logging():
    logging.basicConfig(filename="logs/shark_attack_log.txt", level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    setup_logging()
    
    parser = argparse.ArgumentParser(description="Shark Attack - Advanced Hacking Toolkit")
    
    parser.add_argument('--scan', help="Advanced network scan", action="store_true")
    parser.add_argument('--recon', help="Run reconnaissance tools (Whois, DNS, etc.)", action="store_true")
    parser.add_argument('--sql', help="Test for SQL Injection", action="store_true")
    parser.add_argument('--xss', help="Test for XSS vulnerabilities", action="store_true")
    parser.add_argument('--priv-esc', help="Check for privilege escalation vulnerabilities", action="store_true")
    parser.add_argument('--exploit', help="Run exploitation module", action="store_true")
    parser.add_argument('--post-exploit', help="Post-exploitation (reverse shell, privilege escalation)", action="store_true")
    parser.add_argument('--report', help="Generate report from logs", action="store_true")
    
    args = parser.parse_args()

    try:
        if args.scan:
            target = input("Enter target IP/Domain: ")
            scanner.network_scan(target, config['scanning']['port_range'], config['scanning']['timeout'])
        elif args.recon:
            domain = input("Enter domain for reconnaissance: ")
            recon.run_recon(domain)
        elif args.sql:
            url = input("Enter the target URL for SQL Injection: ")
            sql_injection.check_sql_injection(url)
        elif args.xss:
            url = input("Enter the target URL for XSS detection: ")
            xss_detection.check_xss(url)
        elif args.priv_esc:
            privilege_escalation.check_privilege_escalation()
        elif args.exploit:
            exploit.exploit_target()
        elif args.post_exploit:
            post_exploit.run_post_exploit()
        elif args.report:
            reporting.generate_report()
    except Exception as e:
        handle_error(e)

if __name__ == "__main__":
    main()
