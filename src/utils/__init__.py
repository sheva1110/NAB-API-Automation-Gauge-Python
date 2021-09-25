import logging
import platform

from colorlog import ColoredFormatter
from getgauge.python import data_store

os_name = platform.system()  # Mac: Darwin | Win: Windows
LOG_LEVEL = logging.DEBUG
LOG_FORMAT = "\t%(asctime)-6s %(log_color)s%(levelname)7s | %(log_color)s%(message)s"
LOG_FORMAT_WIN = "\t%(asctime)-6s %(levelname)7s | %(message)s"
logging.root.setLevel(LOG_LEVEL)
logger = logging.getLogger('pythonConfig')  # pylint: disable=invalid-name
logger.propagate = False
if not logger.handlers:
    stream = logging.StreamHandler()  # pylint: disable=invalid-name
    stream.setLevel(LOG_LEVEL)
    if os_name == "Windows":
        formatter = logging.Formatter(LOG_FORMAT_WIN, "%H:%M:%S")
        stream.setFormatter(formatter)
    else:
        stream.setFormatter(ColoredFormatter(LOG_FORMAT, "%H:%M:%S"))  # "%Y-%m-%d %H:%M:%S"
    logger.setLevel(LOG_LEVEL)
    logger.addHandler(stream)


def log_debug(msg):
    if data_store.suite.is_debug:
        logger.debug(msg)


def log_warning(msg):
    if data_store.suite.is_debug:
        logger.warning(msg)
