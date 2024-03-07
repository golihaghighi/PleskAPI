import traceback
import logging
from enum import Enum

# Configure logging
logging.basicConfig(filename='errors.log', filemode='a', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class PleskAPIErrorCode(Enum):
    PLESKAPI_EXTENSION_ERROR = 6001
    PLESKAPI_SERVER_ERROR = 6002
    PLESKAPI_DOMAIN_ERROR = 6003
    PLESKAPI_CLI_ERROR = 6004
    # Define additional error codes as needed


class PleskAPIError(Exception):
    def __init__(self, message="", status_code=None, endpoint=None, request_data=None):
        trace = traceback.extract_stack()[-2]
        self.func_name = trace.name
        self.line_no = trace.lineno
        self.endpoint = endpoint
        self.request_data = request_data

        if status_code:
            error_type = next(
                (code.name for code in PleskAPIErrorCode if code.value == status_code), "Unknown Error")
            error_message = f"{error_type} (Code {status_code}): {message}"
        else:
            error_message = message

        full_message = f"{error_message}. Error occurred in function {self.func_name} at line {self.line_no}, calling endpoint '{self.endpoint}' with data {self.request_data}."

        # Log the error
        logging.error(full_message)

        super().__init__(full_message)
        self.status_code = status_code

    def __str__(self):
        return super().__str__()
