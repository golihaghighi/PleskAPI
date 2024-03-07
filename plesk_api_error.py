import traceback
import logging.handlers
from enum import Enum

# Configure logging with rotation
log_filename = 'errors.log'
log_handler = logging.handlers.RotatingFileHandler(
    log_filename, maxBytes=4*1024*1024, backupCount=5)
log_formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s')
log_handler.setFormatter(log_formatter)

logger = logging.getLogger()
logger.setLevel(logging.ERROR)
logger.addHandler(log_handler)


class PleskAPIErrorCode(Enum):
    EXTENSION_ERROR = 6001
    SERVER_ERROR = 6002
    DOMAIN_ERROR = 6003
    CLI_ERROR = 6004


def log_error(message: str):
    logging.error(message)


class PleskAPIError(Exception):
    def __init__(self, message="", status_code=None, endpoint=None, request_data=None, original_exc=None):
        error_type = "Unknown Error"
        if status_code and status_code in PleskAPIErrorCode._value2member_map_:
            error_type = PleskAPIErrorCode(status_code).name

        trace_info = ''
        if original_exc:
            trace_info = f". Original exception: {str(original_exc)}"

        full_message = f"{error_type} (Code {status_code}): {message}{trace_info}."
        if endpoint and request_data:
            full_message += f" Endpoint: {endpoint}, Data: {request_data}"

        current_stack = traceback.format_exc(limit=1)
        if 'NoneType: None' not in current_stack:
            full_message += f" Stack Trace: {current_stack}"

        log_error(full_message)  # Centralized logging call
        super().__init__(full_message)
        self.status_code = status_code
