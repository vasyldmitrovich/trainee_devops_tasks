import logging
import requests

logging.basicConfig(level=logging.INFO)
logging.info(f"Using requests version: {requests.__version__}")

def square(num):
    return num ** 2

def cube(num):
    return num ** 3

def square_root(num):
    try:
        if num < 0:
            raise ValueError("Cannot take square root of negative number")
        return num ** 0.5
    except TypeError as e:
        logging.error(f"Error taking square root of {num}: {e}")
        return None

def cube_root(num):
    try:
        return num ** (1/3)
    except TypeError as e:
        logging.error(f"Error taking cube root of {num}: {e}")
        return None

values = [4, 16, -1, "invalid"]

if __name__ == "__main__":
    for value in values:
        try:
            result = square(value)
            logging.info(f"Square of {value} is {result}")
        except Exception as e:
            logging.error(f"Error with value {value}: {e}")
