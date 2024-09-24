import logging
import traceback

# Configure the logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger()


def exception_examples():
    logger.info("Starting exception examples...")

    # Example 1: BaseException
    try:
        raise BaseException("This is a BaseException")
    except BaseException as e:
        logger.error(f"Caught an exception: {e}")

    # Example 2: ArithmeticError
    try:
        result = 10 / 0  # This will raise a ZeroDivisionError
    except ArithmeticError as e:
        logger.error(f"Caught an arithmetic error: {e}")

    # Example 3: IndexError
    my_list = [1, 2, 3]
    try:
        value = my_list[5]  # This will raise an IndexError
    except IndexError as e:
        logger.error(f"Caught an index error: {e}")

    # Example 4: ValueError
    try:
        number = int("invalid")  # This will raise a ValueError
    except ValueError as e:
        logger.error(f"Caught a value error: {e}")

    # Example 5: KeyError
    my_dict = {"name": "Alice"}
    try:
        value = my_dict["age"]  # This will raise a KeyError
    except KeyError as e:
        logger.error(f"Caught a key error: {e}")

    # Example 6: FileNotFoundError
    try:
        with open("non_existent_file.txt", "r") as file:
            content = file.read()
    except FileNotFoundError as e:
        logger.error(f"Caught a file not found error: {e}")


# Call the function
exception_examples()
print("---")


def handle_multiple_exceptions():
    logger.info("Starting to handle multiple exceptions...")

    # Trying to perform various operations that might fail
    try:
        value = 10 / 0  # Will cause ZeroDivisionError
        my_list = [1, 2, 3]
        value = my_list[5]  # Will cause IndexError
        number = int("invalid")  # Will cause ValueError
    except (ZeroDivisionError, IndexError, ValueError) as e:
        logger.error(f"Caught an exception: {e}")


# Call the function
handle_multiple_exceptions()
print("---")


def try_except_else_finally():
    logger.info("Starting try/except/else/finally example...")

    try:
        logger.info("Trying to divide...")
        result = 10 / 2  # This will work
    except ZeroDivisionError as e:
        logger.error(f"Caught a division by zero error: {e}")
    else:
        logger.info(f"Division successful, result: {result}")
    finally:
        logger.info("Execution of finally block.")


# Call the function
try_except_else_finally()
print("---")


def raise_statement_example():
    logger.info("Starting raise statement example...")

    try:
        logger.info("Trying to raise an exception...")
        raise ValueError("This is a raised ValueError")
    except ValueError as e:
        logger.error(f"Caught an exception: {e}")
        raise  # Re-raise the exception


# Call the function
try:
    raise_statement_example()
except ValueError as e:
    logger.error(f"Caught the re-raised exception: {e}")
print("---")


def stack_trace_example():
    logger.info("Starting stack trace example...")

    try:
        logger.info("Trying to perform an operation...")
        # Intentional division by zero to trigger an exception
        result = 10 / 0
    except ZeroDivisionError as e:
        logger.error(f"Caught an exception: {e}")

        # Log the stack trace
        logger.error("Stack trace:")
        stack_trace = traceback.format_exc()
        logger.error(stack_trace)


# Call the function
stack_trace_example()
print("---")
