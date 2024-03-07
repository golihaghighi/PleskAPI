from base_plesk_client import BasePleskClient
from plesk_api_error import PleskAPIError


class CliClient(BasePleskClient):
    """
    A client for interacting with CLI-related API endpoints in the Plesk API.
    Extends the BasePleskClient with methods specific to CLI commands.
    """

    def get_commands(self):
        """
        Fetches available CLI commands from the Plesk API.

        Returns:
            dict: A JSON response containing the list of available CLI commands.
        """
        return self.send_request("cli/commands")

    def get_command_ref(self, command):
        """
        Fetches the reference for a specific CLI command.

        Parameters:
            command (str): The name of the CLI command to fetch the reference for.

        Returns:
            dict: A JSON response containing the reference for the specified CLI command.
        """
        if not command:
            # Directly raise PleskAPIError with a meaningful message and optional status_code if necessary
            raise PleskAPIError(
                "Command name must be provided.", PleskAPIError.ERROR_MESSAGES[6004])
        return self.send_request(f"cli/{command}/ref")
