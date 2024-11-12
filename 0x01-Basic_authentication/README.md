# Flask API with Custom Error Handlers and Authentication

## Description

This project implements a Flask API with custom error handlers for unauthorized and forbidden requests. It also introduces a basic authentication system that can be extended to support various authentication mechanisms.

## Requirements

- Python 3.4.3 or later
- Flask
- Flask-CORS

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/your_username/flask_api_auth.git
    cd flask_api_auth
    ```

2. Install the required packages:

    ```sh
    pip3 install -r requirements.txt
    ```

## Usage

### Running the App

Start the Flask app by running:

```sh
API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=auth python3 -m api.v1.app

