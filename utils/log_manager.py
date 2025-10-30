import logging
from datetime import datetime
from pathlib import Path
import colorlog


def setup_logger(log_dir='logs', log_level=logging.INFO):
    """Sets up the logger configuration"""

    project_root = Path(__file__).parent.parent
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    #Create log directory with timestamp
    log_directory=project_root / log_dir / f"logs_{timestamp}"
    log_directory.mkdir(parents=True, exist_ok=True)

    #Create log file path
    log_file_path = log_directory / f"log_{timestamp}.log"

    ## LOGGER CONFIGURATION
    # Get the root logger (or a specific named logger)
    # Using root logger for simplicity here, configure specific loggers if needed
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # HANDLER MANAGEMENT
    # Prevent adding multiple handlers if called multiple times
    if logger.hasHandlers():
        logger.handlers.clear()

    # LOG FORMATTING
    # Define log format
    log_format = '%(asctime)s - %(filename)s:[%(lineno)d] - [%(levelname)s] - %(message)s'
    '''
    %(asctime)s: Timestamp (e.g., 2023-10-05 14:30:45,123)
    %(filename)s: Name of the Python file (e.g., example.py)
    %(lineno)d: Line number in the file (e.g., 42)
    %(levelname)s: Log level (e.g., INFO, WARNING, ERROR)
    %(message)s: The actual log message

    2023-10-05 14:30:45,123 - example.py:[42] - [INFO] - This is a sample log message
    '''

    #Creates a formatter object with this format
    formatter = logging.Formatter(log_format)

    # FILE HANDLER SETUP
    # --- File Handler ---
    file_handler = logging.FileHandler(log_file_path)  # Creates a handler to write logs to a file
    file_handler.setLevel(logging.DEBUG)  # Sets the log level for file output
    file_handler.setFormatter(formatter)  # Applies the formatting to file logs
    logger.addHandler(file_handler)  # # Adds the handler to the logger

    # CONSOLE HANDLER SETUP
    # --- Console Handler ---
    console_handler = colorlog.StreamHandler()
    console_handler.setLevel(log_level)
    console_formatter = colorlog.ColoredFormatter(
        '%(log_color)s' + log_format,
        log_colors={
            'DEBUG': 'cyan', 'INFO': 'green', 'WARNING': 'yellow',
            'ERROR': 'red', 'CRITICAL': 'bold_red',
        }
    )
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)  # Adds the handler to the logger

    logger.info("Logger setup complete.")
    return logger  # Returns the configured logger instance