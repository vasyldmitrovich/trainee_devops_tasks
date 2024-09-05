import logging
import requests
from calculator import Calculator
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logging.info("Info logs")

def create_timestamp_file():
    # Get current timestamp
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

    # Define filename with timestamp
    filename = f"/home/ubuntu/timestamp_{timestamp}.txt"

    # Write the timestamp to the file
    with open(filename, "w") as file:
        file.write(f"Current timestamp: {timestamp}")

def main():
    # Create a file with the current timestamp
    create_timestamp_file()

    # Perform calculations
    calc = Calculator()
    result = calc.add(5, 10)
    logging.info(f"The result of addition is: {result}")
    logging.info(f"Using requests version: {requests.__version__}")
    logging.info("Finish")

if __name__ == "__main__":
    main()

