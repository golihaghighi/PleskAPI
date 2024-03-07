from base_plesk_client import BasePleskClient
from plesk_api_error import  PleskAPIError, PleskAPIErrorCode


class ExtensionsClient(BasePleskClient):
    """Client for extensions-related API calls."""

    def get_extensions(self):
        """Fetches installed extensions."""
        return self.send_request("extensions")

    def get_extension_detail(self, extension_id):
        """Fetches detailed information about a specific installed extension."""
        endpoint = "extensions"  # Specify the endpoint being called
        if not extension_id:
            # Include endpoint and request data (extension_id) in the error message
            raise PleskAPIError(
                message="Extension ID must be provided",
                status_code=PleskAPIErrorCode.EXTENSION_ERROR.value,  # Example status code
                endpoint=endpoint,
                request_data={"extension_id": extension_id}
            ) 
        try:
            return self.send_request(f"{endpoint}/{extension_id}")
        except Exception as e:
            # Catch potential exceptions and raise them as PleskAPIError with context
            raise PleskAPIError(
                message=str(e),
                endpoint=endpoint,
                request_data={"extension_id": extension_id}
            ) from e
