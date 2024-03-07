import pandas as pd
from prettytable import PrettyTable

from cli_client import CliClient
from domains_client import DomainsClient
from extensions_client import ExtensionsClient
from server_client import ServerClient


class PleskRestClient:
    """Aggregates all Plesk API functionalities."""

    def __init__(self, host, username, password, port=8443, protocol='https', verify_ssl=True):
        common_args = {'host': host, 'username': username, 'password': password,
                       'port': port, 'protocol': protocol, 'verify_ssl': verify_ssl}
        self.domains = DomainsClient(**common_args)
        self.server = ServerClient(**common_args)
        self.cli = CliClient(**common_args)
        self.extensions = ExtensionsClient(**common_args)


    def print_response_as_table(self, data, fields):
        """
            Prints the given data in a well-formatted table.

            :param data: A list of dictionaries, where each dictionary represents a row.
            :param fields: A list of strings representing the fields (columns) to include in the table.
        """
        table = PrettyTable()
        table.field_names = fields

        for item in data:
            row = [item.get(field, '') for field in fields]
            table.add_row(row)

        print(table)


    def export_response_to_excel(self, data, fields, file_name='api_response.xlsx'):
        """
            Exports the given API response data to an Excel file.

            :param data: A list of dictionaries, where each dictionary represents a row in the Excel.
            :param fields: A list of strings representing the fields (columns) in the Excel file.
            :param file_name: Name of the Excel file to be created.
        """
        # Create a DataFrame from the data
        df = pd.DataFrame(data, columns=fields)

        # Export DataFrame to Excel
        df.to_excel(file_name, index=False)
        print(f"Data exported to {file_name} successfully.")
