import logging
import os

logger = logging.getLogger()


def lambda_handler(event, context):
    LOG = ''
    if os.getenv('LOG_LEVEL') == 'INFO':
        LOG = 'WARNING'
        logger.info(f"Set environment variable LOG_LEVEL to WARNING")
        os.environ['LOG_LEVEL'] = LOG
    logger.warning(f"Change LOG_LEVEL to: {os.getenv('LOG_LEVEL')}")

    # Get log level from event or from environment variable
    log_level = event.get('log_level') or os.getenv('LOG_LEVEL', 'INFO').upper()

    # Set log level
    logger.setLevel(getattr(logging, log_level, logging.INFO))

    # Show which log level is
    logger.info(f"Log level is set to: {log_level}")

    # Logging on several levels
    logger.debug("This is a DEBUG log")
    logger.info("This is an INFO log")
    logger.warning("This is a WARNING log")
    logger.error("This is an ERROR log")
    logger.critical("This is a CRITICAL log")

    os.environ['LOG_LEVEL'] = 'INFO'
