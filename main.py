import os
from xml import dom
from dotenv import load_dotenv
from plesk_rest_client import PleskRestClient
from plesk_api_error import PleskAPIError


def main():
    # Load environment variables
    load_dotenv()

    # Initialize PleskRestClient with credentials from environment variables
    host = os.getenv('PLESK_HOST')
    username = os.getenv('PLESK_LOGIN')
    password = os.getenv('PLESK_PASSWORD')
    client = PleskRestClient(host, username, password)

    # Attempt to get extension detail and handle possible errors
    try:
        domains = client.domains.get_domains_with_status()
        fields = ["id", "name", "status", "hosting_type", "aliases"]
        client.export_response_to_excel(domains,fields)
    except PleskAPIError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
