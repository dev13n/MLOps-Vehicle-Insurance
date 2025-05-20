# Import necessary modules for logging, file handling, and date/time
import logging
import os
from logging.handlers import RotatingFileHandler  # Enables log file rotation
from from_root import from_root # Utility to get root directory path
from datetime import datetime  # Used to create timestamped log filenames

# Constants for log configuration
LOG_DIR = 'logs'  # Directory where log files will be saved
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  # Log file name with timestamp
MAX_LOG_SIZE = 5 * 1024 * 1024  # Maximum size per log file: 5 MB
BACKUP_COUNT = 3  # Number of backup log files to keep

# Ensure the logs directory exists; create if not
log_dir_path = os.path.join(from_root(), LOG_DIR)
os.makedirs(log_dir_path, exist_ok=True)

# Full path to the log file
log_file_path = os.path.join(log_dir_path, LOG_FILE)

def configure_logger():
    """
    Configures the root logger with:
    - A RotatingFileHandler that saves logs to a file with size limits and backups.
    - A StreamHandler that outputs logs to the console.
    """
    # Create/get the root logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # Set the minimum logging level for the logger

    # Define a standard log message format
    formatter = logging.Formatter("[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s")

    # Setup file handler with rotation
    file_handler = RotatingFileHandler(
        log_file_path, maxBytes=MAX_LOG_SIZE, backupCount=BACKUP_COUNT
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)  # Log all levels to file

    # Setup console handler for immediate feedback
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)  # Show INFO and above in console

    # Add both handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

# Initialize logging configuration when the module is loaded
configure_logger()
