import logging
import os

logger = logging.getLogger()


def lambda_handler(event, context):
    logger.info("New version of lambda")
    log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
    logger.setLevel(getattr(logging, log_level, logging.INFO))

    logger.info("This is an INFO log")
    logger.debug("This is a DEBUG log")

    return {
        'statusCode': 200,
        'body': f"Log level set to: {log_level}",
        'latest': "New version of lambda"
    }
