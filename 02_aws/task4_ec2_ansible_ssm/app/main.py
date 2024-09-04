import logging
import requests
from calculator import Calculator

logging.basicConfig(level=logging.INFO)
logging.info("Info logs")


def main():

    calc = Calculator()
    result = calc.add(5, 10)
    logging.info(f"The result of addition is: {result}")
    logging.info(f"Using requests version: {requests.__version__}")
    logging.info("Finish")

if __name__ == "__main__":
    main()
