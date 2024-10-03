import logging
import argparse
import time


def setup_logging(log_filename):
    logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def process_data(data):
    time.sleep(1)
    logging.info(f"Processing data: {data}")
    return data.upper()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="App to process data and log output.")
    parser.add_argument('--logfile', type=str, default='app_log.txt', help='Log file name')
    args = parser.parse_args()

    time.sleep(1)
    setup_logging(args.logfile)
    process_data("hello")
