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
from PleskRestClient import PleskRestClient

client = PleskRestClient('host', 'username', 'password')
domains = client.domains.get_domains()
print(domains)
```

...

## More Information

For more information and detailed documentation, visit [our website](https://www.webmastersolve.com).

...

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
