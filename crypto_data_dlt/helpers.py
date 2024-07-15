from typing import Optional, Iterable, Dict
from dlt.sources.helpers.rest_client import paginate
from urllib.parse import urljoin
from datetime import datetime

class AlpacaCryptoApi:
    """
    Alpaca Crypto API client for fetching crypto data.
    """

    def __init__(self, base_url: str = "https://data.alpaca.markets") -> None:
        """
        Initialize the Alpaca Crypto API client.

        Args:
            base_url: Base URL for the Alpaca API endpoints.
        """
        self.base_url = base_url

    def fetch_crypto_data(
        self,
        start_date: str,
        end_date: str,
        timeframe: str,
        symbols: str,
        next_page_token: Optional[str] = None
    ) -> Iterable[Dict]:
        """
        Fetch crypto data from Alpaca Crypto API.

        Args:
            start_date: Start date for fetching data.
            end_date: End date for fetching data.
            timeframe: Timeframe for data (e.g., 1Day).
            symbols: Symbols to fetch (e.g., "BTC/USD").
            next_page_token: Token for the next page of results, if available.

        Returns:
            Iterable[Dict]: Generator of crypto data items.
        """
        endpoint = "/v1beta3/crypto/us/bars"
        params = {
            "start": start_date,
            "end": end_date,
            "timeframe": timeframe,
            "symbols": symbols,
            "next_page_token": next_page_token
        }

        url = urljoin(self.base_url, endpoint)

        # Use the paginate() function from the dlt library to handle pagination
        for page in paginate(url, params=params, data_selector="bars"):
            if isinstance(page, list):
                for item in page:
                    if isinstance(item, dict):
                        yield item
                    else:
                        raise ValueError(f"Unexpected item format: {item}")
            else:
                raise ValueError(f"Unexpected page format: {page}")
