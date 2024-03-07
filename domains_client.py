from base_plesk_client import BasePleskClient


class DomainsClient(BasePleskClient):
    """Client for domain-related API calls."""

    def get_domains(self):
        """Fetches a list of domains."""
        return self.send_request("domains")

    def get_domain_status(self, domain_id):
        """Fetches the status of a specific domain by its ID."""
        endpoint = f"domains/{domain_id}/status"
        return self.send_request(endpoint)

    def get_domains_with_status(self):
        """Fetches a list of domains with their statuses."""
        domains = self.get_domains()
        for domain in domains:
            # Assuming each domain dict has an 'id' key
            domain_id = domain["id"]
            status = self.get_domain_status(domain_id)
            domain["status"] = status  # Append status to each domain dict
        return domains
