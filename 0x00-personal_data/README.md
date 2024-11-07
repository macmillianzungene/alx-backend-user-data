# Sensitive Data Logger

## Description

This project implements a logger that obfuscates sensitive information in log messages. It includes functions and classes to filter sensitive data from log records, hash passwords, and validate passwords against their hashes. The project also includes a utility to connect to a secure database and retrieve user data with obfuscated personal identifiable information (PII).

## Requirements

- Python 3.4.3 or later
- Ubuntu 20.04 LTS
- PEP 8 style guide (version 2.5)
- `mysql-connector-python` module
- `bcrypt` module

## Installation

1. Clone the repository to your local machine:

    ```sh
    git clone https://github.com/your_username/sensitive_data_logger.git
    cd sensitive_data_logger
    ```

2. Ensure your files are executable:

    ```sh
    chmod +x filtered_logger.py
    ```

3. Install the required modules:

    ```sh
    pip install mysql-connector-python bcrypt
    ```

## Usage

### Filtering Sensitive Data

The `filter_datum` function obfuscates specified fields in a log message using a regular expression.

```python
import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscates specified fields in a log message.

    Parameters:
    fields (list): List of strings representing fields to obfuscate.
    redaction (str): String to replace the field value with.
    message (str): The log message.
    separator (str): Character separating all fields in the log message.

    Returns:
    str: The obfuscated log message.
    """
    pattern = r'({})=([^{}]+)'.format('|'.join(map(re.escape, fields)), re.escape(separator))
    return re.sub(pattern, r'\1={}'.format(redaction), message)

