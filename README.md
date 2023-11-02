# Polestar

This repository contains all the Polestar API services.

## Installation

1. Install a **Python 3.7** environment.
2. Create a virtual environment using:

    ```bash
    python -m venv env-name
    ```

3. Install all requirements by running:

    ```bash
    pip install --no-cache-dir -r requirements.txt
    ```

## Prerequisite

Start a PostgreSQL instance at **5433** Port.

## Environment Variables

- **POSTGRES_USER**: PostgreSQL User Name
- **POSTGRES_PASSWORD**: PostgreSQL password for the user
- **POSTGRES_HOST**: PostgreSQL host (default: **localhost**)
- **POSTGRES_PORT**: PostgreSQL port (default: **5433**)
- **POSTGRES_DB**: PostgreSQL database name
- **APP_HOST**: Host for the application to run (default: **127.0.0.1**)
- **APP_PORT**: Port for the application (default: **5001**)

## Loading the Data

Run `python3 upload_data.py` to create tables and load all the data into the database.

## Running Tests

Run **test_database.py** to execute all tests.

## How to Run

Activate the virtual environment:

```bash
source venv/bin/activate
```

To start the application, run:

`python3 main.py`

# Accessing the SWAGGER

http://127.0.0.1:5000/api/polestar/swagger


Feel free to adjust any part according to your preferences or specific requirements.



