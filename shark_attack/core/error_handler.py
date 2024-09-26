
import logging

def handle_error(e):
    """ Centralized error handling and logging """
    logging.error(f"An error occurred: {e}")
    print(f"[!] An error occurred: {e}")
