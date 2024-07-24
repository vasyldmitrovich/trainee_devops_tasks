import logging
import sys

# Set the log file name as a command-line argument or use 'logs.txt' as default
log_file = sys.argv[1] if len(sys.argv) > 1 else 'logs.txt'

# Configure the logger with a detailed format
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s'
)

# Function to calculate the square of a number
def square_number(num):
    return num ** 2

# Main program
if __name__ == "__main__":
    # Different numbers to calculate squares for
    numbers = [5, 10, 15, 'err']

    for number in numbers:
        try:
            # Calculate the square of the number
            result = square_number(number)

            # Log an informational message
            logging.info(f'Square of {number} is {result}')

        except Exception as e:
            # Log an error message with additional context about where the error occurred
            logging.error(f'Error in calculation for {number}: {str(e)}')

    # Log a completion message after processing all numbers
    logging.info("Logging completed.")
