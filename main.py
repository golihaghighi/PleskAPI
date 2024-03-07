import os
from dotenv import load_dotenv
import requests
from plesk_rest_client import PleskRestClient



def main():
    # Load environment variables from .env file
    load_dotenv()

    # Access environment variables
    host = os.getenv('PLESK_HOST')
    username = os.getenv('PLESK_LOGIN')
    password = os.getenv('PLESK_PASSWORD')

    client = PleskRestClient(host, username, password)

    try:
        domains = client.domains.get_domains()
        print(domains)
    except requests.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
