# DBT-DLT Ingestion Pipeline

This project demonstrates a data ingestion pipeline using DBT (Data Build Tool) and DLT (Data Load Tool) to fetch and process cryptocurrency data from the Alpaca API. The data is stored in DuckDB, a fast, embeddable database.

## Features

- **Dynamic Date Range**: The pipeline allows you to specify a start and end date for fetching cryptocurrency data, making it flexible and suitable for integration with scheduling tools like Airflow.
- **Automated Unnesting**: Leveraging DLT's capabilities to automatically handle nested data structures, simplifying data transformation and reducing maintenance.
- **Metadata Management**: Metadata about the data fetching operation is stored alongside the crypto data, providing context and traceability.

## Getting Started

### Prerequisites

- Python 3.7+
- [DBT](https://www.getdbt.com/)
- [DLT](https://github.com/data-load-tool/dlt)
- [DuckDB](https://duckdb.org/)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your_username/dbt-dlt-ingestion-pipeline.git
    cd dbt-dlt-ingestion-pipeline
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1. Copy the example secrets file and update it with your own credentials:
    ```bash
    cp example.secrets.toml secrets.toml
    ```

2. Edit `secrets.toml` and add your Alpaca API credentials and DuckDB configuration.

### Running the Pipeline

1. Run the data ingestion pipeline:
    ```bash
    python alpaca_crypto_dlt_pipeline.py
    ```

### Project Structure

- **crypto_data_dlt**: Contains the source and resource definitions for fetching and processing data from the Alpaca API.
- **schemas**: Contains the schema definitions used by DBT.
- **secrets.toml**: Configuration file for storing sensitive information like API keys.

### Example Usage

To fetch and load crypto data for a specific date range, you can call the `load_crypto_data` function with the desired start and end dates:

```python
from alpaca_crypto_dlt_pipeline import load_crypto_data

start_date = "2022-01-01"
end_date = "2024-07-10"

load_crypto_data(start_date=start_date, end_date=end_date)
