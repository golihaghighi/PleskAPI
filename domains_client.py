from base_plesk_client import BasePleskClient


class DomainsClient(BasePleskClient):
    """Client for domain-related API calls."""

    def get_domains(self):
        """Fetches a list of domains."""
        return self.send_request("domains")
