# PleskAPI

The `PleskAPI` is a Python library designed to simplify interactions with the Plesk API, enabling developers to easily manage domains, retrieve server information, and handle errors efficiently.

## Features

- Manage Plesk domains
- Fetch server information
- Custom error handling with detailed messages

## Installation

```bash
git clone https://github.com/golihaghighi/PleskAPI
cd PleskAPI
```

## Usage

```python
import os
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
        extension_details = client.extensions.get_extension_detail('')
        print(extension_details)
    except PleskAPIError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()


```

...

## More Information

For more information and detailed documentation, visit [our website](https://www.webmastersolve.com).

...

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
