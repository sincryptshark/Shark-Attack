
import socket
import logging

def network_scan(target, port_range, timeout):
    logging.info(f"Starting network scan on {target}")
    start_port, end_port = map(int, port_range.split('-'))
    for port in range(start_port, end_port + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(timeout)
            result = s.connect_ex((target, port))
            if result == 0:
                logging.info(f"Port {port}: OPEN")
                print(f"Port {port}: OPEN")
        except Exception as e:
            logging.error(f"Error scanning port {port}: {e}")
        finally:
            s.close()
    logging.info("Network scan completed.")
