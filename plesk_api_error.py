import traceback


class PleskAPIError(Exception):
    ERROR_MESSAGES = {
        6001: "Extension related error",
        6002: "Server related error",
        6003: "Domains related error",
        6004: "CLI related error",
        # Add more specific error codes and messages here
    }
    def __init__(self, message="", status_code=None):
        # Get the stack frame where the exception was instantiated
        trace = traceback.extract_stack()[-2]
        self.func_name = trace.name  # Function name
        self.line_no = trace.lineno  # Line number
        full_message = f"{message} (Function: {self.func_name}, Line: {self.line_no})"
        super().__init__(full_message)
        self.status_code = status_code
        if status_code is not None and status_code in self.ERROR_MESSAGES:
            self.message = f"{self.ERROR_MESSAGES[status_code]} {message}"

    def __str__(self):
        base_message = super().__str__()
        if self.status_code:
            return f"{self.status_code}: {base_message}"
        else:
            return base_message
