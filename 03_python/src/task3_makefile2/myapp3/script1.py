import logging
import os
from datetime import datetime

# Set up logging configuration
log_file = 'script.log'
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def log_script_execution():
    # Get the name of the current script
    script_name = os.path.basename(__file__)

    # Log the message
    logging.info(f'The script "{script_name}" has been executed.')


if __name__ == "__main__":
    log_script_execution()
