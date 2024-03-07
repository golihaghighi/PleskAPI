"""
Module Name: Plesk API Error Handler
Description: Defines a custom exception class for handling Plesk API errors.

This module offers the `PleskAPIError` class, designed to effectively capture and
represent errors from the Plesk API. It extends Python's base Exception class,
adding information specific to Plesk API errors, such as HTTP status codes.
"""

class PleskAPIError(Exception):
    """
    Custom exception class designed to represent errors encountered while interacting with the Plesk API.

    This exception class extends the standard Python Exception class to provide more detailed error information
    specific to Plesk API interactions, including HTTP status codes that may accompany an API response.

    Attributes:
        message (str): A human-readable string describing the error. This attribute is inherited from the base Exception class.
        status_code (int, optional): The HTTP status code associated with the API error, if applicable. This provides additional
                                     context that can be useful for error handling logic.

    Parameters:
        message (str, optional): Descriptive error message. Defaults to an empty string.
        status_code (int, optional): HTTP status code related to the error. Defaults to None.

    Methods:
        __init__: Initializes a new instance of the PleskAPIError class with the specified error message and status code.
        __str__: Returns a string representation of the error, which includes the status code if provided.
    """

    def __init__(self, message="", status_code=None):
        """
        Initializes a new instance of the PleskAPIError class with the provided message and optional HTTP status code.

        Parameters:
            message (str, optional): The error message describing what went wrong.
            status_code (int, optional): An HTTP status code associated with the error from the Plesk API.
        """
        super().__init__(message)  # Initialize the base class with the error message
        # Store the HTTP status code associated with this error
        self.status_code = status_code
