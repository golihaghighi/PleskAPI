"""
Module: Base PleskAPI Client
Description: Provides a Python base interface for making requests to the Plesk API,
             handling authentication, and managing responses, including errors.

This module contains the BasePleskClient class, designed to encapsulate the
common functionalities required for interacting with the Plesk API, including
sending requests and processing responses.
"""

import requests
from requests.auth import HTTPBasicAuth
# Ensure PleskAPIError is properly defined in a separate module
from plesk_api_error import PleskAPIError


class BasePleskClient:
    """
    Base class for interacting with the Plesk API.

    Attributes:
        base_url (str): URL to the Plesk API endpoint.
        auth (HTTPBasicAuth): Authentication credentials for the API.
        verify_ssl (bool): Flag indicating whether SSL certificates should be verified.
        DEFAULT_TIMEOUT (int): Default timeout for API requests.
    """

    DEFAULT_TIMEOUT = 10  # Default timeout for requests in seconds

    def __init__(self, host, username, password, port=8443, protocol='https', verify_ssl=True):
        """
        Initializes the Plesk API client with necessary details.

        Parameters:
            host (str): The server's hostname or IP address.
            username (str): The username for authentication.
            password (str): The password for authentication.
            port (int): The port on which the Plesk API is exposed. Defaults to 8443.
            protocol (str): The protocol used for the API ('http' or 'https'). Defaults to 'https'.
            verify_ssl (bool): Whether to verify the SSL certificate. Defaults to True.
        """
        self.base_url = f"{protocol}://{host}:{port}/api/v2"
        self.auth = HTTPBasicAuth(username, password)
        self.verify_ssl = verify_ssl

    def send_request(self, endpoint, method='GET', data=None):
        """
        Sends a request to a specified endpoint of the Plesk API.

        Parameters:
            endpoint (str): The API endpoint to target.
            method (str): HTTP method to use for the request. Defaults to 'GET'.
            data (dict): The payload for 'POST' requests. Defaults to None.

        Returns:
            dict: The JSON response from the API.

        Raises:
            PleskAPIError: Custom exception indicating an error with the API request.
        """
        url = f"{self.base_url}/{endpoint}"
        headers = {'Content-Type': 'application/json'}

        try:
            # Perform the HTTP request using the requests library
            response = requests.request(method, url, auth=self.auth, headers=headers,
                                        json=data, verify=self.verify_ssl, timeout=self.DEFAULT_TIMEOUT)
            # Check for HTTP errors
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            # Raise a PleskAPIError for any request-related issues
            raise PleskAPIError(
                f"Request error: {e}", status_code=e.response.status_code if e.response else None) from e

        return response.json()
