from base_plesk_client import BasePleskClient


class ServerClient(BasePleskClient):
    """Client for server-related API calls."""

    def get_server_info(self):
        """Fetches server information."""
        return self.send_request("server")
