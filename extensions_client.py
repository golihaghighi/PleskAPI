from base_plesk_client import BasePleskClient
from plesk_api_error import PleskAPIError


class ExtensionsClient(BasePleskClient):
    """Client for extensions-related API calls."""

    def get_extensions(self):
        """Fetches installed extensions."""
        return self.send_request("extensions")

    def get_extension_detail(self, extension_id):
        """Fetches detailed information about a specific installed extension."""
        if not extension_id:
            # Directly raise PleskAPIError with a meaningful message and optional status_code if necessary
            raise PleskAPIError(
                "Extension ID must be provided", PleskAPIError.ERROR_MESSAGES[6001]) 
        return self.send_request(f"extensions/{extension_id}")
