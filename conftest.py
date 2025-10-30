import logging
import pytest

from utils.log_manager import setup_logger


@pytest.fixture(scope="session", autouse=True)
def configure_logging(request):
    """ Sets up logging before any tests run """
    setup_logger() # Configure the logger
    logging.info("Logging configured for test session")