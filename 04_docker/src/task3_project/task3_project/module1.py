import logging
import requests

logging.basicConfig(level=logging.INFO)
logging.info(f"Using requests version: {requests.__version__}")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        logging.error(f"Error dividing {a} by {b}: {e}")
        return None

values = [10, 5, 2, 0, "invalid"]

if __name__ == "__main__":
    for value in values:
        try:
            result = add(value, 2)
            logging.info(f"Add: {value} + 2 = {result}")
        except Exception as e:
            logging.error(f"Error with value {value}: {e}")
