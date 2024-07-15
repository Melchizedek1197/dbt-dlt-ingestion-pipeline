# Alpaca Crypto Data Ingestion Pipeline

The Alpaca Crypto Data Ingestion Pipeline is designed to efficiently fetch and load cryptocurrency data from Alpaca's API into a data destination. This project leverages the `dlt` library to streamline the extraction, transformation, and loading (ETL) process.

## Overview

This pipeline includes functionalities to handle pagination, manage data integrity, and store the data in DuckDB. It is built to fetch cryptocurrency bars data for specified symbols within a given timeframe.

### Supported Endpoint

| Endpoint                                      | Description |
|-----------------------------------------------|-------------|
| `/v1beta3/crypto/us/bars`                     | Retrieves cryptocurrency bars data for specified symbols within a given timeframe. |

## Getting Started

Follow these steps to initialize, configure, and run the Alpaca Crypto Data Ingestion Pipeline.

### Installation

1.Install dependencies:
pip install -r requirements.txt

## Configuration
1-Setup Credentials:

Obtain your Alpaca API key and secret. You can configure them in your environment variables or directly in the alpaca_crypto_dlt_pipeline.py script.

2-Configure Destination:

Modify the destination configuration in the .dlt/secrets.toml and .dlt/config.toml files to specify the DuckDB file path and other credentials.

Example .dlt/secrets.toml:
[sources.alpaca]
api_key = "your_api_key"
secret_key = "your_secret_key"


## Running the Pipeline

1-Initialize the Pipeline:
python alpaca_crypto_dlt_pipeline.py

2-Monitor the Pipeline Execution:

Check the terminal output for any warnings or errors. Ensure that the pipeline completes successfully.

3-Verify Data Ingestion:

Confirm that the data has been loaded into DuckDB or your specified destination by running:
dlt pipeline alpaca_crypto show



