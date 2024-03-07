from domains_client import DomainsClient
from server_client import ServerClient


class PleskRestClient:
    """Aggregates all Plesk API functionalities."""

    def __init__(self, host, username, password, port=8443, protocol='https', verify_ssl=True):
        common_args = {'host': host, 'username': username, 'password': password,
                       'port': port, 'protocol': protocol, 'verify_ssl': verify_ssl}
        self.domains = DomainsClient(**common_args)
        self.server = ServerClient(**common_args)
